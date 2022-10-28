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
    lstfrac = []

    for i in range(N):
        list.append(round(random.uniform(1,10), 2))
        lstfrac.append(round((list[i])*100%100))
    print(list)
    return lstfrac

def MinMax(lstfrac):

    length = length_hint(lstfrac)   
    max = int(list[0])
    for i in range(length):
        if lstfrac[i] > max:
            max = lstfrac[i]

    i = 0
    min = lstfrac[0]
    for i in range(length):    
        if lstfrac[i] > min:
            i+1
        else: min = lstfrac[i]
    print(f'Максимальное значение дробной части= {max}')
    print(f'Минимальное значение дробной части= {min}')

    if max > min:
        result = max-min
    else:
        result = min-max

    return result

list = AddList()
print(list)
print(MinMax(list))