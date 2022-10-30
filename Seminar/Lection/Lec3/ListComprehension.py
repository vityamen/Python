# list=[]
# for i in range(1, 101):
#     if (i % 2 == 0):
#         list.append(i)

# print(list)


# list=[]
# for i in range(1, 101):
#     #if (i % 2 == 0):
#         list.append(i)

# print(list)

list = [i for i in range(1, 10) if i % 2 == 0]
print(list)

list1 = [(i,i) for i in range(1, 10) if i % 2 == 0]
print(list1)

def f(x):
    return x ** 3

list2 = [(i,f(i)) for i in range(1, 10) if i % 2 == 0]
print(list2)

