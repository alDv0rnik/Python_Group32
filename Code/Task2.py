"""
Напишите декоратор @double_it,
который возвращает удвоенный результат вызова декорированной функции

@double_it
def multiply(num1, num2):
    return num1 * num2

@double_it
def get_sum(*args):
    return sum(args)

res = get_sum(1, 2, 3, 4, 5)
print(res) # печатает 30
"""

