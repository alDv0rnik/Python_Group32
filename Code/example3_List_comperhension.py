s = "123"
my_list = [1, 2, 3]
my_list_1 = list(s) # map()
my_list_2 = [i for i in range(1, 4)]

print(my_list)
print(my_list_1)
print(my_list_2)


# new_list = [x.upper() for x in input("Enter a word: ")]
# print(new_list)


number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)

names = ['make', 'john', 'sally']
names = [name.capitalize() for name in names]
print(names)

# Double comperhensions
matrix = [[j for j in range(4)] for i in range(3)]
print(matrix)


