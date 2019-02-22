# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print("Task 1")
def fibonacci(n, m):
    f1 = 1
    f2 = 1
    fib = [f1, f2]
    i=0
    while i <= (m-2):
        if len(fib) >= 2:
            fsum = f1+f2
            f1=f2
            f2=fsum
            fib.append(f1)
            fib.append(f2)
        else:
            continue
        i+=1
    return (fib[n:m+1])

print(fibonacci(2,9))
print("")
print("")

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


#quick Hoar sort   https://proglib.io/p/sort-algorithms/
# def sort_to_max(origin_list):
#     pivot = origin_list[-1]
#     wall = origin_list[0]
#     #current = origin_list[0]
#     j = 0
#     for cur in origin_list:
#         if cur < pivot:
#             vrem = origin_list[0]
#             origin_list = cur
#             cur = vrem
#             j+=1
#         else:
#             continue
#         piv_vrem = pivot
#         pivot
#         wall = origin_list[j]

print("Task 2")
def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):
        for cur in range(len(origin_list)-n):
            if origin_list[cur] > origin_list[cur+1]:
                origin_list[cur], origin_list[cur+1] = origin_list[cur+1], origin_list[cur]
        n += 1
    return(print(origin_list))

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
print("")
print("")

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
print("Task 3")
def filter_my(func, list):
    al = []
    for el in list:
        if func(el) == True:
            al.append(el)
        else:
            continue
    return(al)

list1 = ["8", 3, 'wer', "кукушка", 89, 90.2, -2, "3", '!2wq', "@"]

def func_for_filter(x):
    if isinstance(x, (int, float)):
        return True
    else:
        return False

print("Internal list: ")
print(list1)
print("")
sample = filter_my(func_for_filter, list1)
print("The int and float elements (sample):  ")
for x in sample:
    print(x)
print("")
print("")

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
print("Task 4")

#сумма квадратов диагоналей равна сумме квадратов всех сторон d1^2+d2^2=2(a^2+b^2)
#1) вычислить длины сторон по координатам (по 2 равные стороны д.б.)
#Расстояние между двумя точками равно квадратному корню из суммы квадратов разностей координат по каждой оси
# sqrt(pow((x2-x1), 2)-pow((y2-y1), 2))

# Четырехугольник является параллелограммом, если:
#
# Две его противоположные стороны равны и параллельны. (расстояния)
# Все его стороны попарно равны
# Противоположные углы попарно равны. (через треугольники с диагональю)
# Диагонали точкой пересечения делятся пополам.
import cmath as m

a1x = input("A1 x =     ")
a1y = input("A1 y =     ")

a2x = input("A2 x =     ")
a2y = input("A2 y =     ")

a3x = input("A3 x =     ")
a3y = input("A3 y =     ")

a4x = input("A4 x =     ")
a4y = input("A4 y =     ")

a1 = [float(a1x), float(a1y)]
a2 = [float(a2x), float(a2y)]
a3 = [float(a3x), float(a3y)]
a4 = [float(a4x), float(a4y)]

def isparal(a1, a2, a3, a4):
    a1a2 = m.sqrt(pow((a2[0]-a1[0]), 2)-pow((a2[1]-a1[1]), 2))
    a2a3 = m.sqrt(pow((a3[0]-a2[0]), 2)-pow((a3[1]-a2[1]), 2))
    a3a4 = m.sqrt(pow((a4[0]-a3[0]), 2)-pow((a4[1]-a3[1]), 2))
    a4a1 = m.sqrt(pow((a1[0]-a4[0]), 2)-pow((a1[1]-a4[1]), 2))

    d1 = m.sqrt(pow((a4[0]-a2[0]), 2)-pow((a4[1]-a2[1]), 2))
    d2 = m.sqrt(pow((a3[0]-a1[0]), 2)-pow((a3[1]-a1[1]), 2))

    # Теорема треугольников для нахождения угла по трем сторонам
    cos_alpha1 = (pow(d1,2) - pow(a1a2,2) - pow(a4a1,2))/2*a1a2*a4a1
    alpha1 = m.acos(cos_alpha1)

    cos_beta1 = (pow(d1,2) - pow(a2a3,2) - pow(a3a4,2))/2*a2a3*a3a4
    beta1 = m.acos(cos_beta1)

    cos_alpha2 = (pow(d2,2) - pow(a1a2,2) - pow(a2a3,2))/2*a1a2*a2a3
    alpha2 = m.acos(cos_alpha2)

    cos_beta2 = (pow(d2,2) - pow(a4a1,2) - pow(a3a4,2))/2*a4a1*a3a4
    beta2 = m.acos(cos_beta2)

    if a1a2 == a3a4 and a2a3 == a4a1:
        print("Стороны попарно равны!")
        if alpha1 == beta1 and  alpha2 == beta2:
            print("Противоположные углы попарно равны!")
            print("Это - параллелограмм!")
        else:
            print("Противоположные углы попарно не равны - это не параллелограм...")
    else:
        print("Стороны попарно не равны - это не параллелограм...")

isparal(a1, a2, a3, a4)
