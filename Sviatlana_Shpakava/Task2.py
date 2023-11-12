string = "Ham is tasty"
for index, letter in enumerate(string, start=1):
    if index % 2 == 0 and letter == 'a':
        print('b', end = ' ')
    elif index % 2 == 0:
        print(letter, end = ' ')
    else:
        print('_', end=' ')
