class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def get_area_rect(self):
        return self.a * self.b
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

class Square:
    def __init__(self,a):
        self.a = a
    def get_area_sq(self):
        return self.a**2

class Circle:
    def __init__(self,a):
        self.a = a
    def get_arear_cir(self):
        return (self.a**2)*3.14

rect_1 = Rectangle(2,4)
rect_2 = Rectangle(5,6)
print(rect_1 == rect_2)
sq_1 = Square(7)
sq_2 = Square(8)
cir_1 = Circle(3)
cir_2 = Circle(4)

figures = [rect_1,rect_2,sq_1,sq_2,cir_1,cir_2]
for figure in figures:
    if isinstance(figure,Rectangle):
        print(figure.get_area_rect())
    elif isinstance(figure,Square):
        print(figure.get_area_sq())
    else:
        print(figure.get_arear_cir())