"""
Дан прямоугольный треугольник. На вход подается длина 2-х катетов - a и b.
Найти гипотенузу

с^2 = a^2 + b^2
"""
import math

a = int(input("A: "))
b = int(input("B: "))
print(round(math.sqrt(pow(a, 2) + pow(b, 2)), 2))