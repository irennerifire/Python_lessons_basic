__author__ = 'Вашурина Мария Андреевна'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

a = input("Введите целое число (желательно, много цифр)   ")

print("Цифры числа:  ")

print("цикл for - исходный ввод")
for j in a:
    print(j)

i = 0
print("(цикл while- исходный ввод)")
while i < len(a):
    print(a[i])
    i+=1

a = str(a)
i = 0
print("(цикл while - преобразовали в строку)")
while i < len(a):
    print(a[i])
    i+=1

print("цикл for - преобразовали в строку")
for j in a:
    print(j)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = input("Введите переменную а: ")
b = input("Введите переменную b: ")

c = b #доп. переменная
b = a
a = c

print("Поменяли их местами: a = ", a, "b = ", b)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input("Сколько вам полных лет? Введите цифру: "))

if age >= 18:
    print("Доступ разрешен!")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")
