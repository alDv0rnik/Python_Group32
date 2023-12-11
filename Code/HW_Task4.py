
def reverse_list(active=True):
    def decor(func):
        def wrapper(*args, **kwargs):
            if active:
                res = func(*args, **kwargs)
                return res[::-1]
            return func(*args, **kwargs)
        return wrapper
    return decor


@reverse_list(active=False)
def transform(list1, list2):
    result = []
    for i in list1:
        for j in list2:
            result.append(f"{i} + {j}")
    return result


lst1 = [i for i in range(5)]
lst2 = [j for j in range(5)]

print(transform(lst1, lst2))
