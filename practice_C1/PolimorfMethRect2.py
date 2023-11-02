from PolimorfMethRect import Rectangle,Square

rect_1 = Rectangle (3,4)
rect_2 = Rectangle (5,7)

print(rect_1.get_area_rectangle())
print(rect_2.get_area_rectangle())

sq1 = Square(5)
sq2 = Square(16)

print(sq1.get_area_square(), sq2.get_area_square())

figures = [rect_1,rect_2,sq1,sq2]
for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area_rectangle())