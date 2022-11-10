from time import time

def func(t):
    return int(str(t).split('.')[1]) % 100


if __name__ == "__main__":
    print(func(time()))


