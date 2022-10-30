# def sum(x, y):
#     return x + y

sum = lambda x, y: x + y

def mult(x, y):
    return x * y

def calc(op, a, b):
    print(op(a, b))
    #return (op(a, b))
    
calc(sum, 10, 15)
calc(lambda x, y: x * y, 2, 4)



# def calc(x):
#     return x+10
# # print(calc(10))

# def calc1(x):
#     return x*10

# # print(calc1(10))

# def math(op, x):
#     print(op(x))

# math(calc1, 10)
# math(calc, 10)
