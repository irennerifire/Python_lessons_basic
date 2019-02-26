# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
import re
line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

res = re.findall(r'[^A-Z]+', line)
print(res)

# for x in range(len(line) - 2):
#     trio = line[x:x+3]
#     if trio[1].isupper() and trio[::2].islower():
#         print(trio, "-->", trio[::2])


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

res2 = re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', line_2)
print(res2)




# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import random
import re

lnum = [random.randint(0, 10) for _ in range(0, 2500)]

f = open("nums.txt", "w")
for el in lnum:
    f.write(str(el))
f.close()

#самую длинную последовательность одинаковых цифр
#[0-9]= \d
#\d+ или \d*

file = open("nums.txt", "r")
#line = [l.strip() for l in file]
line_s = file.read()
print(f"Содержимое файла:   {line_s}")

#res3 = range(10)
res3 = []
# for i in range(10):
#     res3.append(i)

#for index, value in enumerate(res3):
# res3[0].extend(max(re.findall(r'[0]*', line_s)))
# res3[1].append(max(re.findall(r'[1]*', line_s)))
# res3[2].append(max(re.findall(r'[2]*', line_s)))
# res3[3].append(max(re.findall(r'[3]*', line_s)))
# res3[4].append(max(re.findall(r'[4]*', line_s)))
# res3[5].append(max(re.findall(r'[5]*', line_s)))
# res3[6].append(max(re.findall(r'[6]*', line_s)))
# res3[7].append(max(re.findall(r'[7]*', line_s)))
# res3[8].append(max(re.findall(r'[8]*', line_s)))
# res3[9].append(max(re.findall(r'[9]*', line_s)))

res3_0 = max(re.findall(r'[0]*', line_s))
res3_1 = max(re.findall(r'[1]*', line_s))
res3_2 = max(re.findall(r'[2]*', line_s))
res3_3 = max(re.findall(r'[3]*', line_s))
res3_4 = max(re.findall(r'[4]*', line_s))
res3_5 = max(re.findall(r'[5]*', line_s))
res3_6 = max(re.findall(r'[6]*', line_s))
res3_7 = max(re.findall(r'[7]*', line_s))
res3_8 = max(re.findall(r'[8]*', line_s))
res3_9 = max(re.findall(r'[9]*', line_s))

res3 = [res3_0, res3_1, res3_2, res3_3, res3_4, res3_5, res3_6, res3_7, res3_8, res3_9]

def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):
        for cur in range(len(origin_list)-n):
            if len(origin_list[cur]) > len(origin_list[cur+1]):
                origin_list[cur], origin_list[cur+1] = origin_list[cur+1], origin_list[cur]
        n += 1
    return(origin_list)

max_str = sort_to_max(res3)
print ("Все найденные последовательности:       ", max_str)

output = [max_str[-1]]

for ind, i in enumerate(reversed(max_str)):
    if len(max_str[8-ind]) == len(i):
        #output.append(max_str[8-ind])
        output.append(i)
        print(output)
        print("ind:  ", max_str[8-ind])
        print("i:  ", i)


print("Максимальная подстрока цифр:     ", output)
