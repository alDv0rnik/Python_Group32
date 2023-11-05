i = 10
# while i > 0:
#     print(i)
#     i -= 1

# for i in range(10, 0, -1):
#     print(i)
# else:
#     print("End of cycle")


# break / continue
# while i > 0:
#     i -= 1
#     if i == 6:
#         print(f"{i} - skipped")
#         continue
#     elif i == 4:
#         print("breaking cycle")
#         break
#     print(i)
# else:
#     print("End")


def some_function():
    pass


# pass statement
# test = "Guru"
# for i in test:
#     if i == 'r':
#         print('Pass executed')
#         pass
#     print(i)


# for in different data structures
l = [1, 2, 3, 4, 5]
# for i in l:
#     print(i)
#
#
# for i in range(len(l)):
#     print(l[i])

# for i, _ in enumerate(l):
#     print(l[i])

l1 = [(1, 2), (3, 4), (5, 6)]
# for a, b in l1:
#     print(a)
#     print(b)

dct = {"a": 1, "b": 2, "c": 3}

for key in dct.keys():
    print(key)
    # print(f"{key} -> {value}")

# GO
# for i := 0; i > 0; i++ {
#
# }

lst = []

for i in range(10):
    lst.append(i)
print(lst)

lst1 = [i for i in range(10)]
print(lst1)
