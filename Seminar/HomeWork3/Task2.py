# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randint
from operator import length_hint

def AddList():
    N = (int(input('Введите размер списка: ')))
    list = []

    for i in range(0,N):
        list.append(i)
    return list

def Multi(list):
    multi = []
    length = length_hint(list)   # определяем длину списка, для взятия элемента с конца
    lenmulti = int((length/2)+0.5)     # задаем длину нового списка, проход до середины списка. 0.5 добавляем для математического округления
    for i in range(lenmulti):
        multi.append(list[i]*list[length-1-i])
    return multi
 

list = AddList()
print(list)
print(Multi(list))