# 1. Напишите программу, которая принимает на вход вещественное число
#  и показывает сумму его цифр.    
#     Пример:    
#     - 6782 -> 23
#     - 0,56 -> 11

digitsum = 0
print('Введите вещественное число: ')
num = str(input())
length = int(len(num))
for i in range(0, length):
    digitnum = float(num[i])
    digitsum = digitsum + digitnum
print(digitsum)    