a = {1,2,3,5,8}
b = {2,5,8,13,21}
c = a.copy() # c = {1,2,3,5,8}
u = a.union(b) # u = {1,2,3,5,8,13,21}
i = a.intersection(b) # i = {8,2,5}
dl = a.difference(b) # dl = {1,3}
dr = b.difference(a) # dr = {13,21}
print(dr)

q = a \
    .union(b)\
    .difference(a.intersection(b))
print(q)

s = frozenset(a)
