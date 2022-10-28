# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141 10^(-1) ≤ d ≤10^(-10)

def InputNumbers(num):
    number = float(input(f"{num}"))
    return number

num1 = InputNumbers("Введите 1 число: ")
num2 = InputNumbers("Введите 2 число: ")
n = int(InputNumbers("Введите точность (количество знаков после запятой): "))
l = lambda num1, num2: num1/num2
result = round(l(num1,num2), n)
print(f"Результат деления:{result}")
