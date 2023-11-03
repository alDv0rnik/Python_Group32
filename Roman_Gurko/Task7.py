# Look at my horse! My horse is amazing!
import math
x1, y1 = int(input("start x: ")), int(input("start y: "))
x2, y2 = int(input("destination x: ")), int(input("destination y: "))
print(1 if x1 != x2 and y1 != y2 and abs(x1 + y1 - x2 - y2) == 3 else 0)