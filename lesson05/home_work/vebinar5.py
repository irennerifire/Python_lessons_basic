import os
import sys

print("Путь - ", sys.argv)

def print_help():
    print("help")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")

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

def ping():
    print("pong")

do = {"help": print_help,
      "mkdir": make_dir,
      "ping": ping}

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
