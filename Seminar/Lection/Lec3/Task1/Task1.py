path = 'file.txt'
f = open(path, 'r')
# data = f.read() + ' '


for i in f:
    print(i)

f.close()
