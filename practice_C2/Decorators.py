# # # class Dog:
# # #     def __init__(self, name, age):
# # #         self.name = name
# # #         self.age = age
# # #
# # #     # создадим свойство human_age, которое будет переводить возраст животного в человеческий
# # #     @property  # тот самый магический декоратор
# # #     def human_age(self):
# # #         return self.age * 7.3
# # #
# # #
# # # jane = Dog("jane", 4)
# # # # т.к. метод помечен декоратором property, то нам не надо вызывать этот метод, чтобы получить результат
# # # print(jane.human_age)
# #
# #
# # class Square:
# #     _a = None
# #     def __init__(self,a):
# #         self.a = a
# #     @property
# #     def a(self):
# #         return self._a
# #     @a.setter
# #     def a(self,value):
# #         if value > 0:
# #             self._a = value
# #     @property
# #     def area(self):
# #         return self.a**2
# # firstSq = Square(7)
# # print(firstSq.area)
#
#
#
# # class Dog:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #     # создадим свойство human_age, которое будет переводить возраст животного в человеческий
# #    # тот самый магический декоратор
# #     @property
# #     def human_age(self):
# #         return self.age * 7.3
# #
# #
# # jane = Dog("jane", 4)
# # print(jane.human_age)
#
# class Dog:
#     _happiness = 10
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def human_age(self):
#         return self.age * 7.3
#
#     # добавим новое поле — шкала счастья
#     @property
#     def happiness(self):
#         return self._happiness
#
#     # с помощью декоратора setter мы можем неявно передать во второй
#     # аргумент значение, находящееся справа от равно, а не закидывать это
#     # значение в скобки, как мы это делали в модуле C1, когда не знали о
#     # декораторах класса
#     @happiness.setter
#     # допустим, мы хотим, чтобы счастье питомца измерялось шкалой от 0 до 100
#     def happiness(self, value):
#         if value <= 100 and value >= 0:
#             self._happiness = value
#         else:
#             raise ValueError("Happiness must be between 0 ... 100")
#
#
# jane = Dog("jane", 4)
# jane.happiness = 100  # осчастливим нашу собаку < :
# print(jane.happiness)


# class Square:
#     def __init__(self,a):
#         self.a = a
#
#     @property
#     def a (self):
#         return self._a
#     @a.setter
#     def a(self,value):
#         if value > 0:
#             self._a = value
#     @property
#     def area (self):
#         return self.a**2
# Square1 = Square(4)
# print(Square1.a)
#
try:
    some_stroke = input("Введите строковое значение: ")
    number = int(some_stroke)
    if some_stroke != number :
        raise ValueError("Неверно")
except ValueError:
    print("Неверное значение")