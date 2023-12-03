# Task 6
def get_number_of_frogs(year: int) -> int:
    F_k = 120
    for i in range(1, year):
        F_k = 2 * (F_k - 50)
    return F_k


print(get_number_of_frogs(3))
