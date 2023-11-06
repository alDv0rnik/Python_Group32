x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
if (abs(x1 - x2) == 1 and abs(y1 - y2) == 2) or (abs(x1 - x2) == 2 and abs(y1 - y2) == 1):
    print("good")
else: print("not good")
