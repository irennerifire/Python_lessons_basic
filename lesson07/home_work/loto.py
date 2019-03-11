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
        bochonki = list(range(91))
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

card = Card()
#print(f"First card line:    {card.line1}")
#print(f"Second card line:    {card.line2}")
#print(f"Third card line:    {card.line3}")
card.card_print()

boch = Bochonok()
b = boch.choice()
