# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

N = int(input('Введите натуральное число: '))

multipl = 2
num_mult = []
while N > 1:
    if N % multipl == 0:
        num_mult.append(multipl)
        N = N / multipl
        multipl = 2
    else:
        multipl += 1
    print(multipl)
print(num_mult)


