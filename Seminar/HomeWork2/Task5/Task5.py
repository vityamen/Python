#5. Реализуйте алгоритм перемешивания списка.

from random import randint

def func():
    list = [1,2,3,4,5,6,7,8,9,10]
    res = []
    for i in range (len(list)):
        index = randint(0, len(list)-1)

        res.append(list[index])

        list.remove(list[index])

    return res

    file.close()    

if __name__ == "__main__":
    print (func())