# https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-open/

### READ FILE

file = open(
    "data/sh.txt",
    mode="r",
    encoding="utf-8"
)
data = file.read()
# print(data[:100])


### READ LINE

file = open("text.txt", "r")
# print(file.readline(2))
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# for _ in range(10000):
    # print(file.readline())

file.close()

### READ LINES

file = open("text.txt", "r")
list_of_lines = list(map(lambda x: x.strip("\n"), file.readlines()))
# print(list_of_lines)
# for line in list_of_lines:
#     if not "2" in line:
#         # print(line)
file.close()


### SEEK/ TEll

with open("text.txt", "r") as file:
    # print(file.tell(), "- Start position")
    file.readline()
    # print(file.tell(), "- New position")
    file.seek(0)
    # print(file.tell())

# file.readline() ValueError: I/O operation on closed file.

### READ PICTURES

with open("data/dog.png", "rb") as file:
    # print(file.read())
    print(file.readline(1))
    print(file.readline(2))
    print(file.readline(3))
    print(file.readline(4))