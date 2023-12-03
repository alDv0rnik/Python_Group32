# Task 8
def get_pairs(lst: list) -> list[tuple]:
    if len(lst) == 1:
        return None
    newlist = lst.pop(0)
    if type(lst[0]) is tuple:
        return lst
    lst.append((newlist, lst[0]))
    return get_pairs(lst)


print(get_pairs([1]))
print(get_pairs([1, 2, 3, 4, 5]))
