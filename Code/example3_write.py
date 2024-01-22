# with open("test.txt", "w") as file:
#     file.write("1234")


lst = ["text1", "text2", "text3"]
with open("test.txt", "a+") as file:
    for elem in lst:
        file.write(elem + "\n")

    # print(file.read())
