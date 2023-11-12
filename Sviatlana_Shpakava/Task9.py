string = "1_2,40_5,5_32"
print([int(number) for elem in string.split(',') for number in elem.split('_')])
