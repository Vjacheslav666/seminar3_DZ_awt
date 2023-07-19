from Seminar3 import print_task as spt
from collections import Counter
from colorama import init
import re

init()
def menu_task():
    print(spt.text_menu())
    numDZ = int(input('\033[33mВведите номер задачи: \033[0m'))
    if 0<= numDZ < 4:
        match numDZ:
            case 0:
                print(spt.exin_text())
                exit()
            case 1:
                print(spt.text_dz1())
                print(find_duplicates())
                menu_task()
            case 2:
                print(spt.text_dz2())
                print(top_10_words())
                menu_task()
            case 3:
                print(spt.text_dz3())
                print(pack_backpack())
                menu_task()
    else:
        print(spt.error_text())
        menu_task()

# Задача 1
def find_duplicates():
    lst = []
    lstNum = int(input('Введите нужное колличество значений в список: '))
    num = 1
    if lstNum == 0:
        print(spt.exin_text())
        menu_task()
    else:
        for _ in range(lstNum):
            n = int(input(f'Введите {num} число: '))
            if 0 < n < 10:
                lst.append(n)
                num += 1
            elif n == 0:
                print(spt.exin_text())
                menu_task()
            else:
                print(spt.error_text())
                find_duplicates()
    print(f'Ваш лист:\n{lst}')
    return list(set([x for x in lst if lst.count(x) > 1]))

# Задача 2
def top_10_words():
    text = input('Введите текст: ')
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)

# Задача 3
def pack_backpack():
    items = {'Тент': 5, 'Вода': 3, 'Еда': 4, 'Одежда': 2, 'Аптечка первой помощи': 1}
    max_weight = 15
    possible_items = []
    for item, weight in items.items():
        if weight <= max_weight:
            possible_items.append(item)
            max_weight -= weight
    return possible_items