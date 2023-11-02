x1, y1 = map(int,input('Введите 2 координаты 1 точки через пробел ').split())
x2, y2 = map(int,input('Введите 2 координаты 2 точки через пробел ').split())
print(1 if x1==x2 or y1==y2 or x1-x2==y1-y2 else 0)
