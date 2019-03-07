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
    def __init__(self, name = "Иван", sname = "Иванович", surname = "Иванов", age = 0):
        self.name = name
        self.sname = sname
        self.surname = surname
        self.age = age

    def info():
        print(f"Ученик {self.name} {self.surname}")
        print(f"{self.age} лет")

class Parent:
    def __init__(self, name = "", sname = "", surname = ""):
        self.name = name
        self.sname = sname
        self.surname = surname

class Mama(Parent):
    def __init__(self, name = "", sname = "", surname = ""):
        super().__init__(name)
        super().__init__(sname)
        super().__init__(surname)
class Papa(Parent):
    def __init__(self, name = "", sname = "", surname = ""):
        super().__init__(name)
        super().__init__(sname)
        super().__init__(surname)

class School:
    def __init__(self, schname = "", schnumber = ""):
        self.name = name
        self.number = number

    def info():
        print(f"School {name} number {number}")

class Class(School):
    def __init__(self, schname = "", schnumber = "", num = "1", letter = "A"):
        super().__init__(schname)
        super().__init__(schnumber)
        self.name = num
        self.sname = letter

class Teacher(School):
    def __init__(self, name = "", sname = "", surname = ""):
        self.name = name
        self.sname = sname
        self.surname = surname

class Subject(School):
    def __init__(self, name = ""):
        self.name = name

class Student(School, Parent):
    def __init__(self, name = "Иван", sname = "Иванович", surname = "Иванов", age = 0):
        self.name = name
        self.sname = sname
        super(Parent).__init__(surname)
        self.age = age

    def info():
        print(f"Ученик {self.name} {self.surname}")
        print(f"{self.age} лет")
