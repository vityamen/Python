# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

list = [0, 0, 5, 1, 2, 2, 3,]
result_list = []
checked_numbers = []
for i in range(len(list)):
    if list[i] not in checked_numbers:
        checked_numbers.append(list[i])
        counter = True
        for j in range(i + 1, len(list)):
            if list[j] == list[i]:
                counter = False
                break
        if counter:
            result_list.append(list[i])

print(result_list)