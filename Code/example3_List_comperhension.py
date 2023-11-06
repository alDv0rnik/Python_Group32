s = "123"
my_list = [1, 2, 3]
my_list_1 = list(s) # map()
my_list_2 = [i for i in range(1, 4)]

# res = []
# for i in range(1, 4):
#     res.append(i)

# print(*my_list)
# print(my_list_1)
# print(type(my_list_2))
# # print(res)
#
# nums = input().split()
# l, *_ = map(int, nums)
# print(l)

# new_list = [x.upper() for x in input("Enter a word: ")]
# print(new_list)


names = ['mike', 'john', 'jane']
print([n.capitalize() for n in names])


print([(i, j.capitalize()) for i, j in enumerate(names)])


# # Double comperhensions
matrix = [[j for j in range(4)] for i in range(3)]
print(matrix)

