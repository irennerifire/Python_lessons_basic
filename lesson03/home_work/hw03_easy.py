# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


# Дробная часть вещественного числа равна остатку от его деления на единицу.
# Целая часть соответственно равна разности самого числа и его дробной части.
# Чтобы сохранить определенное количество разрядов после запятой число следует
# сначала сдвинуть влево на соответствующее число разрядов,
# взять его целую часть и сдвинуть обратно в право на столько же разрядов.
# Сдвиг влево/вправо реализуется умножением/делением на основание системы счисления,
# возведенное в степень равную количеству сдвигаемых разрядов.
from decimal import Decimal

def my_round(num, nd):
    drob = num%1    #**
    print("drob:    ", drob)
    zel = num - drob
    print("zel:    ", zel)
    sdvig1 = drob*(10**nd)
    print("sdvig1:    ", sdvig1)
    drob_sdv = sdvig1%1 #**
    print("drob_sdv:    ", drob_sdv)
    zel_sdv = sdvig1 - drob_sdv
    print("zel_sdv:    ", zel_sdv)
    if drob_sdv >= 0.5:
        zel_sdv += 1
        zel_sdv1 = zel_sdv/(10**nd)+zel
        print("zel_sdv cycle:   ", zel_sdv1)
        #zel_sdv = Decimal(zel_sdv)
        #print("zel_sdv cycle Decimal    :   ", zel_sdv)
        #p = abs(zel_sdv.as_tuple().exponent)
        #print("p:   ", p)
        print(f"Округление с {nd} знаками после запятой числа {num} составило: {zel_sdv1}")
        #print(('{:.%df}' % p).format(zel_sdv))
    else:
        zel_sdv2 = zel_sdv/(10**nd)+zel
        print(f"Округление с {nd} знаками после запятой числа {num} составило: {zel_sdv2} ")


print(my_round(2.1234567, 5))
print(round(2.1234567, 5))
print("")
print(my_round(2.1999967, 5))
print(round(2.1999967, 5))
print("")
print(my_round(2.9999967, 5))
print(round(2.9999967, 5))
print("")


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    numstr = str(ticket_number)
    if numstr.isnumeric() == True:
        if len(numstr) == 6:
            l = list(numstr)
            first = int(l[0]) + int(l[1]) + int(l[2])
            last =  int(l[3]) + int(l[4]) + int(l[5])
            if first == last:
                answer = "Счастливый!"
            else:
                answer = "Не счастливый..."
        else:
            answer = "Ошибка ввода числа"
    else:
        answer = "Ошибка ввода числа"
    return(answer)


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
