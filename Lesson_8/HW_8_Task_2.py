class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c

    def calculate_triangle_area(self):
        area = abs(
            self.a.x * (self.b.y - self.c.y) + self.b.x * (self.c.y - self.a.y) + self.c.x * (self.a.y - self.b.y)) / 2
        return area


class Square:
    def __init__(self, a: Point, b: Point, c: Point, d: Point):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def square_area(self):
        side_length = ((self.a.x - self.b.x) ** 2 + (self.a.y - self.b.y) ** 2) ** 0.5
        area = side_length ** 2
        return area


point1 = Point(0, 0)
point2 = Point(0, 5)
point3 = Point(5, 5)
point4 = Point(5, 0)

triangle = Triangle(point1, point2, point3)
print(f"Triangle square is {triangle.calculate_triangle_area()}")

square = Square(point1, point2, point3, point4)
print(f"Square area is {square.square_area()}")
