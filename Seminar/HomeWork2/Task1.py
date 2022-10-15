# 1. Напишите программу, которая принимает на вход вещественное число
#  и показывает сумму его цифр.    
#     Пример:    
#     - 6782 -> 23
#     - 0,56 -> 11

def SumNum(num):
    sum = 0
    for i in num:
        if i != ".":
         sum += int(i)
    return sum

if __name__ == "__main__":
    number = (input('Введите вещественное число: '))
    Summ = SumNum(number)
    print(Summ)