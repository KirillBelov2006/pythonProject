# Классы и объекты
# Класс - сущность
# Воплощение класса - объект
# Класс - внутри нее есть набор характеристик и действий (методы/функции)
# Реальное воплозение - объект этого класса

# class название класса: (с большой буквы)
#    атрибуты класса
#    методы класса

# class Person:
#     pass
# tom = Person() # объект
# bob = Person() # Также объект


# методы классов == функции )
# Определяет поведение классов

# class Person:
#     def say_greeting(self, message):
#         print(message)
# tom = Person()
# tom.say_greeting('hello')


#свойства класса
#self

#self.атрибут
#self.метод

# class Person:
#     def say(self, message):
#         print(message)
#     def say_hello(self):
#         self.say('hello puppy')
#
# tom = Person()
# tom.say_hello()

#Констуркторы
# __init__
# class Person:
#     def __init__(self):
#         print('Создание объетка Person')
#     def say_hello(self):
#        print('hello')
#
# tom = Person()
# tom.say_hello()

#атрибуты/свойства объекта
#self

# class Person:
#     def __init__(self,name):
#         self.name = name
#         self.age = 23
#
#
# user = Person('Kirill')
# user.company = 'Yota'
# print(user.age)
# print(user.name)
# print(user.company)

#Создание объектов
# class Person:
#     def __init__(self,name):
#         self.name = name
#         self.age = 1
#     def show_info(self):
#         print(f'name: {self.name}, age: {self.age}')
#
#
# user = Person('Kirill')
# user.age = 14
# user.show_info()
#
# Kira = Person('Kira')
# Kira.age = 13
# Kira.show_info()



#Объект класса == экземпляр
#Наследование

# class Geom:
#     name = 'Geom'
#     def coords(self,x1,y1,x2,y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#         self.draw()
#
# class Line(Geom):
#     def draw(self):
#         print('Рисовка линии')
#
#
#
# class Rect(Geom):
#
#
#     def draw(self):
#         print("Рисовка прямоугольника")
#
#
# G = Geom()
# G.coords(1,2,3,5)
# L = Line()
# R = Rect()
# L.coords(1,1,2,2)
# R.coords(1,1,2,2)
# print(L.__dict__)
# print(R.__dict__)
# print(G.__dict__)

some_number = '1 2 3 4 5 6 7'
number_list = some_number.split()
for number in  number_list:
    print(number)