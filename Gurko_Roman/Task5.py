class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5


p1 = Point(1.5, 1)
p2 = Point(1.5, 2)
print(p1.dist(p2))
