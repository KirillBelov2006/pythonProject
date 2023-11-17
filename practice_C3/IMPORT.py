from UNIMPORT import *

def compute():
    r = int(input("Введите радиус круга: "))


    a = int(input("Введите длину прямоугольника: "))
    b = int(input("Введите ширину прямоугольника: "))
    if area_circle(r) > area_rectangle(a,b):
        print("Площадь круга больше площади прямоугольника")
    else:
        print("Площадь прямоугольника больше площади круга")
compute()