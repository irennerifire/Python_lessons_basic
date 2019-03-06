# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Student:
    def __init__(self, name = "Иван", sname = "Иванович", surname = "Иванов"):
        self.name = name
        self.sname = sname
        self.surname = surname

class Mama:
    def __init__(self, name = "", sname = "", surname = ""):
        self.name = name
        self.sname = sname
        self.surname = surname

class Papa:
    def __init__(self, name = "", sname = "", surname = ""):
        self.name = name
        self.sname = sname
        self.surname = surname

class Class:
    def __init__(self, num = "1", letter = "A"):
        self.name = num
        self.sname = letter

class Teacher:
    def __init__(self, name = "", sname = "", surname = ""):
        self.name = name
        self.sname = sname
        self.surname = surname

class Subject:
    def __init__(self, name = ""):
        self.name = name
