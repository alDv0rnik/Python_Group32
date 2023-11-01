#Task 4
from math import sqrt, pow
x1, y1 = map(int,input('Введите 2 координаты 1 точки через пробел ').split())
x2, y2 = map(int,input('Введите 2 координаты 2 точки через пробел ').split())
sum = sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))
print(f'Растояние между точками с координатами {x1}.{y1} и {x2}.{y2} равно {sum}')
