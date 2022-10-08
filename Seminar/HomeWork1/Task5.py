# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве. 
# Пример: - A (3,6); B (2,1) -> 5,09 - A (7,-5); B (1,-1) -> 7,21

def GetDistanceFromCoordinate(xa, ya, za, xb, yb, zb):
    result =((xb-xa)**2+(yb-ya)**2+(zb-za)**2)**0.5
    return result

print("Введите координаты точки А")
userXA = int(input("Введите X: "))
userYA = int(input("Введите Y: "))
userZA = int(input("Введите Z: "))
print("Введите координаты точки В");
userXB = int(input("Введите X: "))
userYB = int(input("Введите Y: "))
userZB = int(input("Введите Z: "))

distance = GetDistanceFromCoordinate(userXA, userYA, userZA, userXB, userYB,userZB)
print(f"Расстояние между точками A[{userXA},{userYA},{userZA}] и B[{userXB},{userYB},{userZB}] = {distance}")
