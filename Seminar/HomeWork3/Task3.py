# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
from operator import length_hint

def AddList():
    N = (int(input('Введите размер списка: ')))
    list = []

    for i in range(N):
        list.append(round(random.uniform(1,10), 2))
    return list

def MinMax(list):

    length = length_hint(list)   
    max = list[0]

    for i in range(length):
        if list[i] > max:
            max = list[i]

    i = 0
    min = list[0]
    for i in range(length):    
        if list[i] > min:
            i+1
        else: min = list[i]
  
    print(f'Максимальный элемент = {max}')
    print(f'Минимальный элемент = {min}')
    result = (round((max*100%100-min*100%100), 0))/100

    return result

list = AddList()
print(list)
print(MinMax(list))