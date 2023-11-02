# class StaticClass:
#
#     @staticmethod  # помечаем метод, который мы хотим сделать статичным декоратором @staticmethod
#     def bar():
#         print("bar")
#
# StaticClass.bar()

class Square:
    def __init__(self,side):
        self.side = side

class SquareFactory:
    @staticmethod
    def get_side(side):
        return  Square(side)
sq1 = SquareFactory.get_side(1)
print(sq1.side)