# Задачи:
# 1. Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётной позиции.

from random import randint

def func():
    ln = 0
    sum = 0
    file = open('File.txt', 'r')

    for line in file:
        ln = int(line) 
        if ln % 2 != 0:
            sum += ln
    print(sum)
    file.close()    

if __name__ == "__main__":
    print(func())