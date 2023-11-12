string = "Ham is tasty"
for i in range(len(string)):
    if i % 2 != 0 and string[i] == 'a':
        print('b', end = ' ')
    elif i % 2 != 0:
        print(string[i], end = ' ')
    else:
        print('_', end = ' ')
