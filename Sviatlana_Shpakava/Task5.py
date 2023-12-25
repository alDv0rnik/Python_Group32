class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        dist = ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
        return dist

p1 = Point(1.5, 1)
p2 = Point(1.5, 1)
print(p1.dist(p2))
p1 = Point(2, 3)
p2 = Point(6, 10)
print(p1.dist(p2))
