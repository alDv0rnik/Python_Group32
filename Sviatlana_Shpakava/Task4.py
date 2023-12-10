# Task 4
def reverse_list(func):
    def wrapper(*args):
        return func(*args[::-1])
    return wrapper

@reverse_list
def transform(list1, list2):
    result = []
    for i in list1:
        for j in list2:
            result.append(f"{i} + {j}")
    return result


print(transform([1, 2], [3, 4]))
