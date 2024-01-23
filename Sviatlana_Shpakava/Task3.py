def show_letters(some_str: str):
    for l in some_str:
        if l.isalpha():
            yield l

str1 = show_letters("e6fjl34df-!.rgh")
print(next(str1))
print(next(str1))
print(next(str1))
