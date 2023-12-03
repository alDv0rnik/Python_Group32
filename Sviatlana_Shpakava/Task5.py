# Task 5
def len_min_word(string):
    """This function returns length of the shortest word"""
    return (min(map(len, string.split())))


print("Длина кратчайшего слова: ", len_min_word("python pytho pyth pyt py"))
