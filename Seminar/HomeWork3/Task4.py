# 4. Напишите программу, которая будет преобразовывать десятичное число
# в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def bincode(number):
    bin =''
    while number > 0:
        bin = str( number % 2) + bin
        number = number // 2
    return bin

if __name__ == "__main__":
    number = int(input('Введите десятичное число: '))
    print(bincode(number))