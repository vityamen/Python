# 2. Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def inputValue(n):
    list = []
    for i in range(0,3):
        list.append(input(f"Введите значение {i}: "))
    print(list)
    return list

def checkStatment(n):
    left = not (n[0] or n[1] or n[2])
    right = not n[0] and not n[1] and not n[2]
    result = left == right
    return result

statement = inputValue(3)

if checkStatment(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")