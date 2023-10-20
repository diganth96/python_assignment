class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

# Usage example
shape = Shape()
square = Square(4)

print("Area of a generic shape:", shape.area())  # This will print 0
print("Area of a square with length 5:", square.area())  # This will print 25
