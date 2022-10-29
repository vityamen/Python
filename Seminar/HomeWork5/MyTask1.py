# 1. Создайте программу для игры с конфетами человек против человека.    
#  Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход
# друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем
# 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?    
#     a) Добавьте игру против бота    
#     b) Подумайте как наделить бота "интеллектом"   

import random
from time import time

candy = 2021

def range():                        #случайное число для жеребьевки  
    # return int(str(t).split('.')[1]) % 10             
    return random.randint(0,100)

def ChangePlayer(name1, name2):     #выбор кто первый
    number1 = range()
    print(number1)
    number2 = range()
    print(number2)
    if (number1 > number2):
        print(f'Первым ходит: {name1}')
        firstplayer = name1
        return firstplayer
    else:
        print(f'Первым ходит: {name2}')
        firstplayer = name2
    return firstplayer

def PlayGame(candy, firstplayer):     
    if firstplayer == 'Comp':
        PlayWithComp()
    else:
        left_candy = candy
        while left_candy > 0 and True:
            choose_candy = int(input(f'{firstplayer}, сколько конфет убрать? '))
            if choose_candy <= left_candy and 0 < choose_candy <= 28:
                left_candy = left_candy - choose_candy
                print(f'Остаток конфет: {left_candy}')
                if left_candy <= 0:
                    print(f'Победил:{firstplayer}')
                    break
            else: 
                print('Вы ввели не верное число конфет')
                continue

            if firstplayer == name1:
                firstplayer = name2
            else:
                firstplayer = name1
        else: 
            print(f'Победил:{firstplayer}')

def PlayWithComp(candy, firstplayer):
    left_candy = candy
    while left_candy > 0 and True:
        if firstplayer == 'Comp':
            if left_candy > 100:                    #интелект компьютера
                print(f'{firstplayer}, Сколько конфет убрать?')
                choose_candy = 28
                print(f'Comp решил убрать {choose_candy} конфет')
            else:    
                print(f'{firstplayer}, Сколько конфет убрать?')
                choose_candy = random.randint(1, 28)
                print(f'Comp решил убрать {choose_candy} конфет')
            if choose_candy <= left_candy:
                left_candy = left_candy - choose_candy
                print(f'Остаток конфет: {left_candy}')
            if left_candy <= 0:
                print(f'Победил:{firstplayer}')
                break
            else:
                print(f'Проверка игрока: {firstplayer}')
                
                firstplayer = name1
                
                
        else:
            while left_candy > 0 and True: 
                    choose_candy = int(input(f'{firstplayer}, сколько конфет убрать? '))
                    if choose_candy <= left_candy and 0 < choose_candy <= 28:
                        left_candy = left_candy - choose_candy
                        print(f'Остаток конфет: {left_candy}')
                        
                    else: 
                        print('Вы ввели не верное число конфет')
                        continue
                    if left_candy <= 0:
                        print(f'Победил:{firstplayer}')
                        break
                    else:
                        firstplayer = 'Comp'
                        break

name1 = input('Введите имя первого игрока: ')
name2 = input('Введите имя второго игрока: ') # для игры с компьютером задать имя Comp
result = ChangePlayer(name1, name2)
print(f'{name1}, {name2}')

# if __name__ == '__main__':
if (name1== 'Comp' or name2 == 'Comp'):
    PlayWithComp(candy, result)  # игра с компом 
else:
    PlayGame(candy, result)    # игра с другом
    