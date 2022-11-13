# colors = ["red","green","blue"] # запись в файл
# data = open("file.txt", "w")
# data.writelines(colors)
# data.close()

path = "file.txt"               # чтение файла
data = open(path, "r")
for line in data:
    print(int(line)*10)
data.close()