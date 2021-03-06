# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

l = []

# for _ in range(10):
#     l.append(random.randint(-10, 10))

l = [random.randint(-10, 10) for _ in range(10)]
print("List:    ", l)

quadro = list(map(lambda el: el*el, l))
print("Quadro:  ", quadro)
print("")

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
import re

l1 = ["banana", "apple", "ananas", "papaya", "panapple"]
l2 = ["peech", "lichi", "apple", "panapple"]

new = list(set(l1) & set(l2))
print(new)
print("")

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

num = [random.randint(-100, 100) for _ in range(1, 1000)]
print("Список случайных целых чисел:    ", num)

new_num = [el for el in num if el%3==0 and el%4!=0 and el>0]

print("Список чисел удовлетворяющих всем 3-м условиям:      ", new_num)
