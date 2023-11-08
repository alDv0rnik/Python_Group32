"""
ROT13 — это простой шифр, который заменяет каждую букву строки буквой,
которая находится на 13 букв после неё в алфавите. Программа получает на вход строку,
необходимо зашифровать её с помощью ROT13 и вывести результат.
"""
import string

message = "Ave Cesar"
n = 13

alphabet = string.ascii_lowercase

print(alphabet)
res = ""

for char in message.lower():
    if char in alphabet:
        index = alphabet.index(char.lower())
        new_index = (index + 13) % len(alphabet)
        res += alphabet[new_index]
    else:
        res += char
print(res)