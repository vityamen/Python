# a, b = 3, 4
b = (16,)           # без , будет объявлено число, а не кортеж
a = (3, 4, 6, 41)   # неизменяемый список
print(a)
# print(a[1])
print(a[-2])
# a[0] = 12  # будет ошибка
print(a[0])
print(b)

t = tuple(["red", "green", "blue"])
for e in t:
    print(e)

red, green, blue = t
print("r:{} g:{} b:{}".format(red, green, blue))