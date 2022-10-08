# 3. Напишите программу, которая принимает на вход координаты
#    точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
#    плоскости, в которой находится эта точка (или на какой оси она
#    находится).    
#     Пример:    
#     - x=34; y=-30 -> 4
#     - x=2; y=4-> 1
#     - x=-34; y=-30 -> 3


def GetQuoterFromCoordinate(x, y):
    result = 0
    if (x > 0 and y > 0 ):
        result = 1
    elif (x < 0 and y > 0):
        result = 2
    elif (x < 0 and y < 0):
        result = 3
    elif (x > 0 and y < 0):
        result = 4
    else:
       print(f"X и У не должны быть равны 0 вы ввели {x} {y}")
    return result

userX = int(input("Введите X: "))
userY = int(input("Введите Y: "))

quoter = GetQuoterFromCoordinate(userX, userY)
print(f"координаты[{userX},{userY}] находятся в {quoter} четверти")