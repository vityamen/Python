# Задачи:
# 1. Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётной позиции.

list = [1, 2, 3, 4]
sum=0
for i in range(len(list)):
    if i % 2 != 0:
        sum = sum + list[i]
print(sum)