# # Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.

with open("first_polinom.txt", "r") as file:
    first_polinom = file.read()
with open("second_polinom.txt", "r") as file:
    second_polinom = file.read()


def to_tuple(my_string):
    my_string = str.replace(my_string, "- ", "+ -").split()
    my_string = list(filter(lambda x: x != "+" and x != "=" and x != "0", my_string))
    for i in range(len(my_string)):
        my_string[i] = my_string[i].split("*")
    return my_string


first_polinom = to_tuple(first_polinom)
second_polinom = to_tuple(second_polinom)

sum_polinom = first_polinom + second_polinom
for i in range (len(sum_polinom)):
    if len(sum_polinom[i]) == 1:
        sum_polinom[i] = [sum_polinom[i].pop(0), "X^0"]
cash = []
answer = []

print(sum_polinom)

for i in range(len(sum_polinom)):
    key = sum_polinom[i][1]
    if key not in cash:
        cash.append(key)
        current_sum = int(sum_polinom[i][0])
        for j in range(i + 1, len(sum_polinom)):
                if key == sum_polinom[j][1]:
                    current_sum += int(sum_polinom[j][0])
        answer.append([current_sum, key])


for i in range(len(answer)):
    answer[i] = str(answer[i][0]) + "*" + str(answer[i][1])
answer = str(" + ".join(answer))

answer = str.replace(answer, "+ -", "- ")
answer = str.replace(answer, "*X^0", "")
answer = str.replace(answer, "1*", "")

answer += " = 0"

with open("answer.txt", "w") as file:
    file.write(answer)