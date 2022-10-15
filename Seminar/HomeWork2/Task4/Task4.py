# 4. Задайте список из N элементов, заполненных числами из промежутка 
# [-N, N]. Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

def func(Number):
    list = []
    num = 1
    
    for i in range(Number):
        list.append(randint(-Number, Number))

    file = open('File.txt', 'r')
    
    for line in file:
        num *= list[int(line)]
    print(list)
    print(num)
    file.close()    

if __name__ == "__main__":
    Number = int(input('Введите число: '))
    func(Number)