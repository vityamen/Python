# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве. 
# Пример: - A (3,6); B (2,1) -> 5,09 - A (7,-5); B (1,-1) -> 7,21

def GetDistanceFromCoordinate(xa, ya, xb, yb):
    result =((xb-xa)**2+(yb-ya)**2)**0.5
    return result

print("Введите координаты точки А")
userXA = int(input("Введите X: "))
userYA = int(input("Введите Y: "))
print("Введите координаты точки В");
userXB = int(input("Введите X: "))
userYB = int(input("Введите Y: "))

distance = GetDistanceFromCoordinate(userXA, userYA, userXB, userYB)
print(f"Расстояние между точками A[{userXA},{userYA}] и B[{userXB},{userYB}] = {distance}")
