x1, y1 = int(input("start x: ")), int(input("start y: "))
x2, y2 = int(input("destination x: ")), int(input("destination y: "))
print(1 if x1 == x2 or y1 == y2 or (x1 + y1 == x2 + y2) or (x1 - x2 == y1 - y2) else 0)
