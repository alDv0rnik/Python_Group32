import math

x1, y1 = int(input("Enter x1: ")), int(input("Enter y1: "))
x2, y2 = int(input("Enter x2: ")), int(input("Enter y2: "))
length = math.sqrt(pow(x2 - x1, 2)+pow(y2 - y1, 2))
print("Length between dots is", length)