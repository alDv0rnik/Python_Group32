def get_number_of_frogs(year: int) -> int:
    if year == 1:
        return 120
    return (get_number_of_frogs(year - 1) - 50) * 2


print(get_number_of_frogs(3))
