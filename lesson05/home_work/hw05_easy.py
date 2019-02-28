# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys

print("Путь - ", sys.argv)

def print_help():
    print("help")
    print("mkdir <dir_name> - создание директории")
    print("rmdir <dir_name> - удалить директорию")
    #print("ping - тестовый ключ")

#dir_name = input("Введите директорию: ")

def make_dir():
    if not dir_name:
        print("укажите имя дирректории")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print(f"директория {dir_name} создана")
    except FileExistsError:
        print(f"директория {dir_name} уже существует")

def remove_dir():
    if not dir_name:
        print("укажите имя дирректории")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print(f"директория {dir_name} удалена")
    except FileExistsError:
        print(f"директория {dir_name} не существует")


def make_dir2(dir_name):
    if not dir_name:
        print("укажите имя дирректории")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print(f"директория {dir_name} создана")
    except FileExistsError:
        print(f"директория {dir_name} уже существует")

def remove_dir2(dir_name):
    if dir_name:
        dir_name = dir_name
        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
            os.rmdir(dir_path)
            print(f"директория {dir_name} удалена")
        except FileExistsError:
            print(f"директория {dir_name} не существует")
    else:
        print("укажите имя дирректории")
        return

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir():
    dir_path = os.path.abspath(os.curdir)
    try:
        print(os.listdir(dir_path))
        print(f"Все файлы в дирректории: {dir_path}")
    except FileExistsError:
        print("Ошибка!")

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil as sh

def copy_file():
    if not dir_name:
        print("укажите имя дирректории")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        sh.copy(__file__, dir_name)
        print(f"Файл {__file__} скопирован в дирректорию: {dir_name}")
    except FileExistsError:
        print("Ошибка!")

do = {#"dir": dir_name,
      "help": print_help,
      "mkdir": make_dir,
      "rmdir": remove_dir,
      "listdir": list_dir,
      "copy": copy_file}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("задан неверный ключ")
        print("напишите help")
