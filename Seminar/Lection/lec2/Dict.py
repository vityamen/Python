dictionary = {}
dictionary = \
    {
        'up': "вверх",
        'Left': '<',
        'right': '>',
        'down': 'вниз'
    }
print(dictionary)
print(dictionary['Left'])

for k in dictionary.keys():
    print(k)
print('\n')
for k in dictionary.values():
    print(k)
print('\n')
for item in dictionary:
    # print(dictionary[item])
    print('{}: {}'.format(item, dictionary[item]))
    dictionary['up'] = 'HI'
print(dictionary['up'])

