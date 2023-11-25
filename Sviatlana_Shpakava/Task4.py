# Task 4
def what_is_it(num):
    if num % 2 == 0:
        return "Четное"
    elif num == 0:
        return "0"
    else:
        return "Нечетное"


print(what_is_it(int(input("Введите число: "))))
