# 5. Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так:
#  [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

fib1 = fib2 = 1 
k = int(input())
list =[]
  
for i in range(0, k+1):  
    if(i == 0):
        list.append(0)
    elif(i == 1 or i == 2):
        list.append(1)
    else:
        fib1, fib2 = fib2, fib1+fib2 
        list.append(fib2)

i=k
neglist =[]
for j in range(-k, 0): 
    if(j == 0):
        i -=1
        neglist.append(0)
    if(j == -2 or j == -1):
        neglist.append(int((-1)**(j+1)))
        i -=1
    else:
        neglist.append(int(list[i]*(-1)**(j+1)))
        i -=1
print(neglist+list)
