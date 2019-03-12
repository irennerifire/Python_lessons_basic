#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""
import random


class Bochonok:
    def __init__(self, bochonki = []):
        self.bochonki = Bochonok.spisok(self)

    def spisok(self):
        bochonki = list(range(1, 92))
        return bochonki

    def choice(self):
        bochonok = random.choice(self.bochonki)
        self.bochonki.remove(bochonok)
        print(f"Выпал бочонок: {bochonok}. Осталось бочонков: {len(self.bochonki)}")
        return bochonok


class Card:
    def __init__(self, line1 =[], line2=[], line3=[]):
        self.line1 = Card.card_line(self)
        self.line2 = Card.card_line(self)
        self.line3 = Card.card_line(self)


    def card_line(self):
        line_elements =[random.randint(0, 91) for _ in range(5)]
        line_new = []

        i = 0
        while i < 9:
            line_new.append(0)
            i +=1

        for num in line_elements:
            line_new.remove(0)
            line_new.append(num)

        random.shuffle(line_new)
        return line_new


    def line_preprocess(self, line):
        for i in range(len(line)):
            if line[i] == 0:
                line[i] = " "
        return line

    def card_print(self):
        line1 = Card.line_preprocess(self, self.line1)
        line2 = Card.line_preprocess(self, self.line2)
        line3 = Card.line_preprocess(self, self.line3)
        print("--------------------------------")
        print('  '.join(map(str, line1)))
        print('  '.join(map(str, line2)))
        print('  '.join(map(str, line3)))
        print("--------------------------------")
        # МОЖНО ПОПРОБОВАТЬ ЗАПИСЫВАТЬ ЗНАЧЕНИЯ В МАТРИЦУ И ВЫВОДИТЬ МАТРИЦУ!!!

    def cross_out_card(self, card_line, bochonok):
        flag = 0
        for i in range(len(card_line)):
            if card_line[i] == bochonok:
                card_line[i] = "-"
                flag = 1
        return card_line, flag

    def num_line_count(self, line):
        num_count = 0
        for n in line:
            if n != " " and n != "-":
                num_count += 1
        return num_count

    def win_or_not(self, card):
        line1 = card.line1
        line2 = card.line2
        line3 = card.line3
        num1 = Card.num_line_count(self, line1)
        num2 = Card.num_line_count(self, line2)
        num3 = Card.num_line_count(self, line3)
        win = ""
        if num1 == 0 and num2 == 0 and num3 == 0:
            win = "yes"
        else:
            win = "no"
        return win


class Computer:
    def __init__(self):
        pass

    def take(self):
        computer_card = Card()
        print("---------Карта компьютера-----------")
        computer_card.card_print()
        return computer_card


class Igrok:
    def __init__(self, name = ""):
        self.name = Igrok.get_name(self)

    def get_name(self):
        name = input("Как изволите к Вам обращаться?    -   ")
        return name

    def take_card(self):
        igrok_card = Card()
        print("------------Ваша карта--------------")
        igrok_card.card_print()
        return igrok_card


person = Igrok()
comp = Computer()
boch = Bochonok()

print("")
print(f"Начинем игру, {person.name}!")
print("")
person_card = person.take_card()
print("")
computer_card = comp.take()
print("")

def step(person_card, computer_card, bochonok):
    b = bochonok.choice()
    print("------------Ваша карта--------------")
    person_card.card_print()
    print("")
    print("---------Карта компьютера-----------")
    computer_card.card_print()
    print("")
    computer_card.line1 = computer_card.cross_out_card(computer_card.line1, b)[0]
    computer_card.line2 = computer_card.cross_out_card(computer_card.line2, b)[0]
    computer_card.line3 = computer_card.cross_out_card(computer_card.line3, b)[0]

    #действия пользователя
    print("Посмотрите внимательно на свою карту. Если на ней есть числа, которые можно зачеркнуть, то введите цифру 1 - 'зачеркнуть', если нет - введите цифру 2 - 'продолжить'.")
    move = input("Ваш выбор:    ")

    try:
        if move == "1":
            line1 = person_card.cross_out_card(person_card.line1, b)
            line2 = person_card.cross_out_card(person_card.line2, b)
            line3 = person_card.cross_out_card(person_card.line3, b)

            if line1[1] == 0 and line2[1] == 0 and line3[1] == 0:
                print("Вы ошиблись! В Вашей карте не было чисел, равных номеру бочонка. Вы проиграли...")
                raise SystemExit
            else:
                person_card.line1 = line1[0]
                person_card.line2 = line2[0]
                person_card.line3 = line3[0]
                print("Ход сделан")

        elif move == "2":
            line1 = person_card.cross_out_card(person_card.line1, b)
            line2 = person_card.cross_out_card(person_card.line2, b)
            line3 = person_card.cross_out_card(person_card.line3, b)

            if line1[1] == 1 or line2[1] == 1 or line3[1] == 1:
                print("Вы ошиблись! В Вашей карте были числа, равные номеру бочонка. Вы проиграли...")
                raise SystemExit
            else:
                print("Ход сделан")
                pass
        else:
            print("Введен неверный вариант ответа!")
            exit(0)
    finally:
        print(" ")


def make_step(person, computer_card, person_card, bochonok):
    cwin = computer_card.win_or_not(computer_card)
    pwin = person_card.win_or_not(person_card)

    if cwin == "yes":
        print("Компьютер выиграл!")
    elif pwin == "yes":
        print(f"Вы, {person.name}, выиграли!")
    else:
        step(person_card, computer_card, bochonok)

    return cwin, pwin

step_flag = ["", ""]
while step_flag[0] != "yes" or step_flag[1] != "yes":
    step_flag=make_step(person, computer_card, person_card, boch)
    if step_flag[0] == "yes":
        break
    elif step_flag[1] == "yes":
        break
