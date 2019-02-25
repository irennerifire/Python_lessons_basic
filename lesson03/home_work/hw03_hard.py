# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# Логика:
#1) ЗП / 100 - 1% от всей оплаты       (но как бы 100% - это норма часов...)
#2) Для каждого работника высчитать процент выполненной работы:
#       кол-во отработанных часов / общее кол-во часов нормы для работника * 100%
#3) Сравнить кол-во отработанных часов с нормой часов:
#       а) если часов меньше нормы, то
#               ЗП = процент работы * олата 1 процента работы (п. 1)
#       б) если часов больше нормы, то
#               (не очень понятно про удвоенную зп...)
#               переработка % = (часы работы - норма)|норма_часов*100%
#               удвоенная зп за 1 % = норма_ЗП*2/ 100
#               ЗП = стандартная ЗП + (удвоенная зп за 1 %)*(переработка%)

import os
import pandas as pd

#fdir = os.path.dirname(os.path.realpath("C:/Users/root/GeekBrains/python_basic/lesson03/home_work"))
#path = os.path.join(fdir, "data/workers.csv")

workers = pd.read_csv("data/workers.csv", sep="\s+")
print(workers)
workers = workers.sort_values(["Фамилия"], ascending=[True])
print("Отсортировали по алфавиту фамилии: ")
print(workers)
print("")
hours = pd.read_csv("data/hours_of.csv", sep="\s+")
print(hours)
hours = hours.sort_values(["Фамилия"], ascending=[True])
print("Отсортировали по алфавиту фамилии: ")
print(hours)
print("")

workers["1%_ЗП"] = workers["Зарплата"]/100
print(workers)

workers["процент_работы"] = hours["Отработано_часов"]/workers["Норма_часов"]*100
print(workers)

print(hours)
workers["Отработано_часов"] = hours["Отработано_часов"].copy()

#Сама запуталась в присваиваниях... Почему-то меняются кол-вом
#отработанных часов Дуров и Грибов при обоих вариантах... Хотя и отсортировала нормально

# for w in workers["Фамилия"]:
#     if (w == hours["Фамилия"]).all(axis=0):
#         workers.iloc[w.index,8] = hours.iloc[w.index, 3]
print(workers)
if (workers["Отработано_часов"] < workers["Норма_часов"]).all(axis=0):
    workers["Итоговая_ЗП"] = workers["1%_ЗП"]*workers["процент_работы"]
else:
    workers["Переработка"] = (workers["Отработано_часов"] - workers["Норма_часов"])/workers["Норма_часов"]*100
    workers["Итоговая_ЗП"] = workers["Зарплата"]+2*workers["1%_ЗП"]*workers["Переработка"]
print(workers)
print(hours)
print("Итоговая зарплата составила:   ")
print(workers[["Фамилия", "Итоговая_ЗП"]])


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
