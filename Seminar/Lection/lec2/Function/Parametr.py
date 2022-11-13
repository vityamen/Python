import re


def concatenatio(*params):
    res: str = "" # явное прописание типа данных стринг
    for item in params:
        res += item
    return res

print(concatenatio('a','s','d','w'))
print(concatenatio('a','1'))
