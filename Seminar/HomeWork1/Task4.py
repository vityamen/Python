# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y)

def GetCoordinateFromQuoter(quoter):
    if (quoter == 1 ):
        print('x и y от 0 до бесконечности')
    elif (quoter == 2):
        print('x < 0 и y от 0 до бесконечности')
    elif (quoter == 3):
        print('x < 0 и y < 0')
    elif (quoter == 4):
        print('x > 0 и y < 0')
    else:
       print("Вы ввели не существующий номер четверти")
    

quoter = int(input("Введите номер четверти: "))
print(f'диапазон координат находящихся в {quoter} четверти =')
GetCoordinateFromQuoter(quoter)