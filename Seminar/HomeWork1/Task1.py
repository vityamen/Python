# Задачи:
# 1. Напишите программу, которая принимает на вход цифру,
#  обозначающую день недели, и проверяет, является ли этот день выходным.    
#     Пример:    
#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

print('введите число N')
N = int(input())

def whichday(N):
    if N<6 and N>1: return 'будни'
    elif N>6 and N<8: return 'выходной'
if whichday(N) == 'будни':
    print('да')
else:
    print('нет')