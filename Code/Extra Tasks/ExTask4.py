"""
На вход подается строка. Проверить является ли она палиндромом.
Использование срезов и функции reverse() запрещено
"""

txt = input()
print("Non palindrome" if [1 for i in range(len(txt)) if txt[i] != txt[len(txt) - 1 - i]] else "Palindrome")


