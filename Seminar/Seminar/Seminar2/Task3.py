# 3. Напишите программу, в которой пользователь будет задавать две строки,
#  а программа - определять количество вхождений одной строки в другой.

firststr = str(input('Введите первую строку: '))
secondstr = str(input('Введите вторую строку: '))

count = 0
index = 0
start = index
while index != -1:
    if firststr.find(secondstr, start+1)!=-1:
        index = firststr.find(secondstr, start+1)
        start = index
        count +=1
    else: 
        index = -1
print(count)
