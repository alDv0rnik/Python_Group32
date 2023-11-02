x1, y1 = map(int,input('Введите 2 координаты 1 точки через пробел ').split())
x2, y2 = map(int,input('Введите 2 координаты 2 точки через пробел ').split())
print(1 if (abs(x1-x2)==3 and abs(y1-y2)==1) or (abs(x1-x2)==1 and abs(y1-y2)==3) else 0)
