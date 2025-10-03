import math


class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        return None

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        return round(pow(self.radius,2) * math.pi,2)


def print_area(shape):
    print(f"The area of {shape.name} is {shape.area()}")
rect = Rectangle(20,40)
circ = Circle(20)

print_area(rect)
print_area(circ)


