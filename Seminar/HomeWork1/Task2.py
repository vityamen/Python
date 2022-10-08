# 2. Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def inputValue(n):
    list = []
    for i in range(n):
        list.append(input(f"Введите значение {i}: "))
    return list

def checkStatment(n):
    left = not (n[0] or y[1] or z[2])
    right = not n[0] and not n[1] and not n[2]
    result = left == right
    return result

statement =inputValue(3)

if checkStatment(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")