class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def display(self):
        print(f"({self.x}, {self.y})")


point1 = Point(2, 3)
point2 = Point(4, 5)

point3 = point1 + point2

point3.display()