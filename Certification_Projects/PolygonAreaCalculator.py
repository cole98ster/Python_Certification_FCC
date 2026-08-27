import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (self.width + self.height)*2

    def get_diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)
    
    def get_picture(self):
        current_width = self.width
        current_height = self.height
        if current_width > 50 or current_height > 50:
            return "Too big for picture."
        if current_height < 2 or current_width < 2:
            return "Too small for image"
        Print = ''
        iterate = 0
        while iterate < (self.height):
            Print += (self.width * "*") + "\n"
            iterate += 1
        return Print
    
    def get_amount_inside(self,shape):
        width_division = int(self.width / shape.width)
        height_division = int(self.height / shape.height)
        if width_division < 1 or height_division < 1:
            return 0
        else:
            return width_division * height_division
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_height(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side
    
    def __str__(self):
        return f"Square(side={self.side})"


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))