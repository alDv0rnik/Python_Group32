# roman_numbers_map = {
#     1: "I",
#     5: "V",
#     10: "X",
#     50: "L",
#     100: "C",
#     500: "D",
#     1000: "M"
# }
#
#
# # def arabic_to_roman(n: int):
# #     thousand = n // 1000
# #     hundred = (n - 1000 * thousand) // 100
# #     ten = ((n - 1000 * thousand) - 100 * hundred) // 10
# #     units = ((n - 1000 * thousand) - 100 * hundred) - 10 * ten
# #     return thousand, hundred, ten, units
#
# def roman_to_arabic(roman: str) -> int:
#     res = 0
#     roman_map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
#     others = ["CD", "CM", "XL", "XC", "IV", "IX"]
#     for i in range(len(roman)):
#         if i < len(roman) - 1 and (roman[i] + roman[i+1]) in others:
#             res -= roman_map[roman[i]]
#         else:
#             res += roman_map[roman[i]]
#     return res
#
#
# def arabic_to_roman(n):
#     values = [1000, 900, 800, 500, 400, 100, 90, 80, 50, 40, 10, 9, 8, 5, 4, 1]
#     symbols = ["M", "CM", "DCCC", "D", "CD", "C", "XC", "LXXX", "L", "XL", "X", "IX", "VIII", "V", "IV", "I"]
#     result = ""
#     for i in range(len(values)):
#         value = values[i]
#         while n >= value:
#             n -= value
#             result += symbols[i]
#     return result
#
#
# print(roman_to_arabic("MCMXC"))
# print(arabic_to_roman(1666))


class HistoryDict(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__history = [*kwargs.keys()]
        self.__count = 0

    def get_history(self):
        return self.__history

    def set_values(self, key, value):
        if self.__contains__(key):
            key = str(key) + f"{self.__count + 1}"
            self.__setattr__(key, value)
            self.__history.append(key)
            self.__count += 1
        else:
            self.__setattr__(key, value)
            self.__history.append(key)


d = dict(bar=4)
hd = HistoryDict(foo=42, bar=4)
print(d)
print(hd.__dict__)
print(hd.get_history())



