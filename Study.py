# st1 = {1, 2, 3}
# st2 = {4, 5, 6}
# print(set.union(st1,st2))

# S = 0
# n = 1
#
# while S ** 2  < 1000:
#     S += n
# print(S)
#
# n = 1
# while True:  # в данной программе это условие всегда True, цикл будет бесконечным
#     print("Kirill")
#     n += 1
#     if n > 10:
#         break
#
# def n_and_a(a,n):
#     if a % n == 0:
#         print("n является делителем числа а")
#     else:print("n не является делителем числа a")
# n_and_a(4,2)
# n_and_a(5,3)


# any_number1 = int(input("Введите первое значение: "))
# any_number2 = int(input("Введите второе значение: "))
# if any_number1 > any_number2:
#     print(any_number1,"Больше",any_number2)
# else:
#     print(any_number2, "Больше" ,any_number1)

# any_number = int(input("Введите значение: "))
# if any_number % 2 == 0:
#     print("Значение чётное")
# else:
#     print("Значение нечетное")


# a = int(input("Введите первое большее число: "))
# b = int(input("Введите второе меньшее число: "))
# c = a % b
# d = a / b
# if a%b == 0:
#     print('Число "а" кратно числу "b".', '\nРезультат деления:', int(d), end='.')
# else:
#     print('Число "a" некратно числу "b".\nОстаток от деления:', c, end='.')

# one_l_bottle = int(input("Введите кол-во бутылок 1 литра и меньше: "))
# more_l_bottle = int(input("Введите кол-во бутылок больше 1 литра: "))
#
# small = 0.10
# large = 0.25
#
# refund = one_l_bottle * small + more_l_bottle * large
# print("Ваша выручка составит $%.2f."% refund)


# sum_order = float(input("Введите сумму заказа в ресторане: "))
#
# waiter = sum_order * 0.18
# print("Чаевые официанту = %.2f"%waiter)
# tax = sum_order * 0.05
# print("Налог = %.2f"%tax)
#
# server_plus_tax = sum_order + waiter + tax
# print("Чаевые и налог = %.2f"%server_plus_tax)


# n = int(input("Введите положительное число: "))
# summa = n * (n+1) / 2
# print("Сумма первых", n, "положительных чисел =",summa)

# souvenir_weight = 75
# some_things_weight = 112
#
# souvenirs = int(input("Введите кол-во сувениров: "))
# some_things = int(input("Введите кол-во безделушек: "))
#
# all_weight = souvenir_weight * souvenirs + some_things_weight * some_things
# print(all_weight,"Вес в граммах")

# colors = 'red green blue'
# colors_split = colors.split() # список цветов по-отдельности
# print(colors_split)
# colors_joined = ' and '.join(colors_split) # объединение строк
# print(colors_joined)


# first_dep = int(input("Введите сумму изначального депозита: "))
#
# first_year = 0.04
# second_year = 0.04 + 0.04
# third_year = 0.04 + 0.04*2
#
# first_percent = first_dep * first_year + first_dep
# print("Сумма за первый год = %.2f"%first_percent)
#
# second_percent = first_dep * second_year + first_dep
# print("Сумма за второй год = %.2f"%second_percent)
#
# third_percent = first_dep * third_year + first_dep
# print("Сумма за третий год = %.2f"%third_percent)

# import math
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# summa = a + b
# difference = a - b
# composition = a * b
# chastnoe = a / b
# ostatok = a % b
# Log = math.log10(a)
# stepen = a ** b
# All_operations = summa, difference, composition, chastnoe, ostatok, Log, stepen
# print(All_operations)


# b = float(int(input("Введите длину основания треугольника: ")))
# h = float(int(input("Введите высоту треугольника: ")))
#
# area =  (b * h) / 2
# print("S треугольника =",area)


# any_number = int(input("Введите четырёхзначное число-"))
# summa = 0
# while any_number != 0:
#     p = any_number % 10
#     summa += p
#     any_number = any_number // 10
# print(summa)


# any_number = int(input("Введите значение: "))
# if any_number % 2 == 0:
#     print("Число чётное")
# else:
#     print("Число нечётное")


# any_age = int(input("Введите возраст: "))
# if any_age <= 0:
#     print("Возраст неверный")
# elif any_age == 1:
#     print(10.5)
# elif any_age == 2:
#     print(10.5+10.5)
# else:
#     print((21+(any_age*4)))


# any_letter = input("Введите букву латинского алфавита: ")
# any_list = ["a","e","i","o" and "u"]
# if any_letter in any_list:
#     print("Буква гласная")
# elif any_letter == "y":
#     print("Буква может быть гласной или согласной")
# else:
#     print("Это буква согласная")

# sides = int(input("Введите кол-во сторон фигуры: "))
# if sides == 3:
#     print("Треугольник")
# elif sides == 4:
#     print("Четырёхугольник")
# elif sides == 5:
#     print("Пятиугольник")
# elif sides == 6:
#     print("Шестиугольник")
# elif sides == 7:
#     print("Семиугольник")
# elif sides == 8:
#     print("Восьмиугольник")
# elif sides == 9:
#     print("Девятиугольник")
# elif sides == 10:
#     print("Десятиугольник")
# else:
#     print("Кол-во сторон не подходит")

# months = int(input("Введите номер месяца:"))
# if months == 1:
#     print("в месяце 31 день")
# elif months == 2:
#     print("в месяце 28 или 29 дней ")
# elif months == 3:
#     print("в месяце 31 день ")
# elif months == 4:
#     print("в месяце 30 дней ")
# elif months == 5:
#     print("в месяце 31 день ")
# elif months == 6:
#     print("в месяце 30 дней")
# elif months == 7:
#     print("в месяце 31 день ")
# elif months == 8:
#     print("в месяце 31 день ")
# elif months == 9:
#     print("в месяце 30 дней")
# elif months == 10:
#     print("в месяце 30 дней ")
# elif months == 11:
#     print("в месяце 30 дней ")
# elif months == 12:
#     print("в месяце 31 день ")
#


# noise = int(input("Введите уровень шума в дБ: "))
# if noise == 40:
#     print("Тихая комната")
# elif noise == 70:
#     print("Будильник")
# elif noise == 106:
#     print("Газовая газонокосилка")
# elif noise == 130:
#     print("Отбойный молоток")
# elif 40<noise<=69:
#     print("Будильник или Тихая комната")
# elif 70<noise<=105:
#     print("Будильник или Газовая газонокосилка")
# elif 106<noise<=129:
#     print("Газовая газонокосилка или Отбойный молоток")
# else:
#     print("Значение уровня шума вне диапозона")


# a = int(input("Введите длину стороны a: "))
# b = int(input("Введите длину стороны b: "))
# c = int(input("Введите длину стороны c: "))
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b != c or a != b == c or a != c == b or b != c == a:
#     print("Треугольник равнобедренный")
# elif a != b != c:
#     print("Треугольник разносторонний")


# x = int(input("Введите целое число (0 для выхода): "))
# # Запускаем цикл, пока пользователь не введет ноль
# while x != 0:
#     if x > 0:
#         print("Это положительное число.")
#     else:
#         print("Это отрицательное число.")


# num = float(input("Введите число: "))
# # Сохраняем подходящее значение в переменной result
# if num == 0:
#     result = "Введен ноль"
# if num != 0:
#     result = "Введен не ноль"
# # Отобразим результат
# print(result)


# nominal = str(input("Введите номинал банкноты: "))
# if nominal =="1$":
#     print("На банкноте изображен Джордж Вашингтон")
# elif nominal == "2$":
#     print("На банкноте изображен Томас Джефферсон")
# elif nominal == "5$":
#     print("На банкноте изображен Авраам Линкольн")
# elif nominal == "10$":
#     print("На банкноте изображен Александр Гамильтон")
# elif nominal == "20$":
#     print("На банкноте изображен Эндрю Джексон")
# elif nominal == "50$":
#     print("На банкноте изображен Улисс Грант")
# elif nominal == "100$":
#     print("На банкноте изображен Бенджамин Франклин")
# else:
#     print("Ошибка")


# Month = int(input("Введите месяц: "))
# Day = int(input("Введите день: "))
# if Month == 1 and Day == 1:
#     print("Новый год")
# elif Month == 7 and Day == 1:
#     print("День Канады")
# elif Month == 12 and Day == 25:
#     print("Рождетсво")
# else:
#     print("На эту дату нет праздников")


# digit = int(input("Введите цифру на шахматной доске: "))
# letter = str(input("Введите букву на шахматной доске: "))
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# digits = range(1, 9)
#
# if letter not in letters:
#     print('Not in list, use A-H')
# elif digit not in digits:
#     print('Not in list, use 1-8')
# else:
#     letter_index = letters.index(letter)
#     digit_index = digits.index(digit)
#     if letter_index % 2 == digit_index % 2:
#         print('Black')
#     else:
#         print('White')


#
# a = 0
# b = 0
#
# while id(a) == id(b):
#     a -= 1
#     b -= 1
#
# print(a)


# some_text = input("Введите текст: ")
# some_text=list(set(some_text))
#
# print("Уникальных символов:",len(some_text))


# digit = int(input("Введите число: "))
# if type(digit) == int and digit in range(1,100) and digit % 2 == 0 and digit % 3 == 0:
#     print("Число подходит")
# else:
#     print("Число не подходит")

#
# stroke = "abcdef"
# print(stroke[::2])


# number = 12345
# number = str(number)
# print(number[::-1])

# mas = ['Это просто строка','http://golos.io','Ещё одна строка','http://golosboard.ru']
# for i in mas:
#     if i[:4] == 'http':
#         print(i)

# Month = input("Введите месяц вашего рождения: ")
# Day = int(input("Введите день вашего рождения: "))
# if Month == "Декабрь" and 22<=Day<=31 or Month == "Январь" and 1<=Day<=19:
#     print("Козерог")
# elif Month == "Январь" and 20<=Day<=31 or Month == "Февраль" and 1<=Day<=18:
#     print("Водолей")
# elif Month == "Февраль" and 19<=Day<=29 or Month == "Март" and 1<=Day<=20:
#     print("Рыбы")
# elif Month == "Март" and 21<=Day<=31 or Month == "Апрель" and 1<=Day<=19:
#     print("Овен")
# elif Month == "Апрель" and 20<=Day<=30 or Month == "Май" and 1<=Day<=20:
#     print("Телец")
# elif Month == "Май" and 21<=Day<=31 or Month == "Июнь" and 1<=Day<=20:
#     print("Близнецы")
# elif Month == "Июнь" and 21<=Day<=30 or Month == "Июль" and 1<=Day<=22:
#     print("Рак")
# elif Month == "Июль" and 23<=Day<=31 or Month == "Август" and 1<=Day<=22:
#     print("Лев")
# elif Month == "Август" and 23<=Day<=31 or Month == "Сентябрь" and 1<=Day<=22:
#     print("Дева")
# elif Month == "Сентябрь" and 23<=Day<=30 or Month == "Октябрь" and 1<=Day<=22:
#     print("Весы")
# elif Month == "Октябрь" and 23<=Day<=31 or Month == "Ноябрь" and 1<=Day<=21:
#     print("Скорпион")
# elif Month == "Ноябрь" and 22<=Day<=30 or Month == "Декабрь" and 1<=Day<=21:
#     print("Стрелец")

# rating_of_employee = float(input("Введите рейтинг сотрудника из таблицы: "))
# salary = 2400
# if rating_of_employee == 0.0:
#     print("Низкий Уровень\nПрибавка к зарплате = 0\nЗарплата = 2400.00")
# elif rating_of_employee == 0.4:
#     print("Средний уровень\n""Прибавка к зарплате =",2400.00*0.4,"\nЗарплата =",(2400*0.4) + 2400)
# elif rating_of_employee == 0.6 or rating_of_employee > 0.6:
#     print("Высокий уровень\n""Прибавка к зарплате =", 2400.00 * 0.6, "\nЗарплата =", (2400 * 0.6) + 2400)
# else:
#     print("Неверное значение")

# for i in range(10, 1000):
#     digits = [int(digit) for digit in str(i)]
#     if len(digits) >= 2 and digits[0] + digits[1] == 5:
#         print(i)
# x = int(input("Введите значение: "))
# while x != 0:
#     if x > 0:
#         print("Это положительное число.")
#     else:
#         print("Это отрицательное число.")
#
# x = int(input("Введите целое число (0 для выхода): "))


# message = input("Введите сообщение (оставьте его пустым для выхода): ")
# # Начало цикла, пока сообщение не станет пустым
# while message != "":
#     n = int(input("Сколько раз повторить сообщение? "))
#     for i in range(n):
#         print(message)
# # Запрашиваем следующее сообщение
# message = input("Введите сообщение (оставьте его пустым для выхода): ")


# numbers = [-1, 2, -3, 4, -5, 6, -7, 8, -9]
#
# positive_numbers = [ i for i in numbers if i > 0]
#
# print(positive_numbers)


# some_stroke = "Hey,What's your favorite movie?"
# some_stroke = list(some_stroke)
# print(sorted(some_stroke[:-2]))

# something = ["Достака","Борщ.html","window.html","block"]
# for i in something:
#     if i.endswith("html"):
#         print(i)


# P = 1
# N = 5
# for i in range(1, N+1):
#     print("Значение суммы на предыдущем шаге: ", P)
#     print("Текущее число: ", i)
#     P *= i
#     print("Значение суммы после сложения: ", P)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: сумма равна = ", P)


# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print("Значение суммы на предыдущем шаге: ", S)
#     print("Текущее число: ", i)
#     S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
#     print("Значение суммы после сложения: ", S)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: сумма равна = ", S)

# N = 5
#
# for i in range(1, N + 1):
#    print("*" * i)

# def print_ladder(n):
#     if n == 3:
#         for i in range(n):
#             i+=1
#             print("*"*i)
#     elif n == 4:
#         for i in range(n):
#             i+=1
#             print("*"*i)
# print_ladder(4)
# print("Сумма за третий год = %.2f"%third_percent)

# price = [4.95, 9.95, 14.95, 19.95, 24.95]
# for x in price:
#     print(x, f'{x*0.6:.{2}f}', f'{x-x*0.6:.{2}f}')

# marks ={ 'A+': 4.0, 'C+': 2.3,
#     'A':  4.0, 'C':  2.0,
#     'A-': 3.7, 'C-e': 1.7,
#     'B+': 3.3, 'D+': 1.3,
#     'B':  3.0, 'D':  1.0,
#     'B-': 2.7, 'F':  0
# }
# print(marks.get(input('Буквенная оценка: '), 'Неизвестная оценка'))

# lens = int(input("Введите длину волны:"))
# if 380<=lens<450:
#     print("Фиолетовый")
# elif 450<=lens<495:
#     print("Синий")
# elif 495<=lens<570:
#     print("Зеленый")
# elif 570<=lens<590:
#     print("Желтый")
# elif 590<=lens<620:
#     print("Оранжевый")
# elif 620<=lens<=750:
#     print("Красный")
# else:
#     print("Неверное значение")
import datetime

# def print_2_add_2():
#     print(2+2)
# print_2_add_2()
#
# def hello_world():
#     print("Hello world")
# hello_world()

# limit = int(input("Введите целое число: "))
# # Выводим все числа, кратные трем, вплоть до указанного пользователем значения
# print("Все числа, кратные трем, вплоть до", limit, ":")
# for i in range(3, limit + 1, 3):
#  print(i)
#
# %.2f"% %.2f"%server_plus_tax
# sale = 0.6
# purchase = [4.95, 9.95,14.95,19.95,24.95]
# for i in purchase:
#     print(round(i,2),"Изначальная цена", round(i * 0.6, 2),"Цена со скидкой",round(i-i*0.6,2),"Размер скидки")
#
#
# for i in range(101):
#     f = int(9/5)*i +32
#     print(f'C-{i}, F-{f}')

# a = int(input("Первое значение: "))
# # b = int(input("Второе значение: "))
# # if a and b < 0:
# #     print("Ложные переменные")
# a = int(input("Введите значение"))
# if all([type(a) == int,
#         100 <= a <= 999,
#         a % 2 == 0,
#         a % 3 == 0]):
#     print("Число удовлетворяет условиям")

# number = 12345
# reversed_number = 0
#
# while number != 0:
#     digit = number % 10
#     reversed_number = reversed_number * 10 + digit
#     number //= 10
#
# print("Перевёрнутое число:", reversed_number)

# digit_list = [1,-4,2,-6,4,6,-11,7,8]
# for i in digit_list:
#     if i > 0 :
#         print(i)
#
# some_list = [1.456,2.125,3.32,4.1,5.34]
# for i in some_list:
#     print(round(i,1),end=", ")

# some_dict = {"a":1,"b":2,"c":3,"d":4,}
# print(list(some_dict.values()))

# def check_last_first(word1, word2):
#     last_char = word1[-1].lower()  # Получаем последнюю букву первого слова (приведенную к нижнему регистру)
#     first_char = word2[0].lower()  # Получаем первую букву второго слова (приведенную к нижнему регистру)
#
#     return last_char == first_char  # Возвращаем True, если буквы совпадают, и False в противном случае
#
#
# # Пример использования функции
# word1 = "Hello"
# word2 = "orange"
# result = check_last_first(word1, word2)
# print(result)

# def linear_solve(a, b):
#     if a: # помним, что 0 интерпретируется как False, иначе True
#         return b / a
#     elif not a and not b:
#         return "Бесконечное кол-во корней"
#     else:
#         return "Нет корней"
# edibles = ["отбивные", "пельмени", "яйца", "орехи"]
# for food in edibles:
#     if food == "пельмени":
#         print("Я не ем пельмени!")
#         break
#     print("Отлично, вкусные " + food)
# print("Ужин окончен.")

# some_dict = {"a":1,"b":2,"с":3,"d":4,}
# print(list(some_dict.keys()))

# a = int(input("Введите значение: "))
# b = int(input("Введите значение: "))
# count = 0
# for i in range(a,b+1):
#     print(i)
#     count+=1
# print("Кол-во чисел",count)

# candies_kg = float(input("Стоимость 1 кг конфет: "))
# cost = 0
# for i in range(1,11):
#     cost=candies_kg*i
#     print("Стоимость",i,"кг","конфет =",cost)
# a = int(input("Введите кол-во минут за месяц: "))
# b = int(input("Введите кол-во сообщений за месяц: "))
# if a == 50 and b == 50:
#     print("Оплата за тариф $15,00 ")
# elif a > 50:
#     for i in range (a+1):
#         i= (i*0.25+a)-a
#         print(i,i)

# class User:
#     pass
# peter = User()
# peter.name = "Peter Robertson"
#
# julia = User()
# julia.name = "Julia Donaldson"
# print(peter.name)
# print(julia.name)
#
# peter.email = "peterrobertson@mail.com"
# print(peter.email)
# print('\n')
# print(julia.email)

# class User:
#     pass
# kirill = User()
# kirill.name = "Kirill Belov"
# kirill.email = "kirill.belov2043@mail.ru"
#
# liza = User()
# liza.name = "Liza Kustulidi"
# liza.email = "liza.kustulidi@mail.ru"
#
# print(kirill.name)
# print(kirill.email)
# print("\n")
# print(liza.name)
# print(liza.email)

# class Product:
#     def __init__(self,name,category,quantity_in_stock):
#         self.name = name
#         self.category = category
#         self.quantity_in_stock = quantity_in_stock
#     def is_available(self):
#         return True if self.quantity_in_stock > 0 else False


# some_number = int(input("Введите число: "))
# if some_number % 2 == 0:
#     print("Число четное")
# else:
#     print("Нечетное")


# letter = input("Введите букву латинского алфавита: ")
# num_lis = list("a","e","i","o","u")
# if letter == "a" or letter == "e" or letter == "i" or \
#         letter == "o" or letter == "u":
#     print("Буква гласная")
# elif letter == "y":
#     print("Буква может быть гласной или согласной")
# else:
#     print("Введена согласная буква")

# for i in range(5):
#     print(i+1,end=" " )
#
# for i in range(10):
#     if i % 2 == 0:
#         print(i  )

# a = 8
# b = 1
# while (a>5):
#     a = a-2
#     b = b + a
#     print(b)


# colors = 'red green blue'
# colors_split = colors.split()
# print(colors_split)
# colors_joined = ' and '.join(colors_split)
# print(colors_joined)

# some_number = int(input("Введите диапозон: "))
# for i in range(some_number):
#     print(i)

# class User:
#     pass
#
# peter = User()
# peter.name = "Peter Robertson"
# peter.email = "peterrobertson@mail.com"
#
# julia = User()
# julia.name = "Julia Donaldson"
# julia.email = "juliadonaldson@mail.com"
#
#
#
# print(peter.name,"\n",peter.email,end=" ""\n")
# print(julia.name,"\n",julia.email)

# class Product:
#     def __init__(self, name, category, quantity_in_stock):
#         self.name = name
#         self.category = category
#         self.quantity_in_stock = quantity_in_stock
#
#     def is_available(self):
#         return True if self.category == "food" else False
# eggs = Product("eggs", "food", 5)
# print(eggs.is_available())


# class Event:
#     def __init__(self, timestamp, event_type, session_id):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
# events = [
#     {
#      "timestamp": 1554583508000,
#      "type": "itemViewEvent",
#      "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#      "timestamp": 1555296337000,
#      "type": "itemViewEvent",
#      "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#      "timestamp": 1549461608000,
#      "type": "itemBuyEvent",
#      "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
# ]
#
#
# for event in events:
#     event_obj = Event(timestamp=event.get("timestamp"),
# 	              event_type=event.get("type"),
# 		      session_id=event.get("session_id"))
#     print(event_obj.type)


import datetime


# class Product:
#     max_quantity = 100000
#
#     def __init__(self, name, category, quantity_in_stock):
#         self.name = name
#         self.category = category
#         self.quantity_in_stock = quantity_in_stock
#
#     def is_available(self):
#         return True if self.quantity_in_stock > 0 else False
#
#
# class Food(Product):
#     is_critical = True
#     needs_to_be_refreshed = True
#     refresh_frequency = datetime.timedelta(days=1)
#
#
# eggs = Food(name="eggs", category="food", quantity_in_stock=5)
# print(eggs.max_quantity)
# print(eggs.is_available())


# class Event:
#     def __init__(self, timestamp, event_type, session_id):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
# events = [
#     {
#      "timestamp": 1554583508000,
#      "type": "itemViewEvent",
#      "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#      "timestamp": 1555296337000,
#      "type": "itemViewEvent",
#      "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#      "timestamp": 1549461608000,
#      "type": "itemBuyEvent",
#      "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
# ]
#
#
# for event in events:
#     event_obj = Event(timestamp=event.get("timestamp"),
# 	              event_type=event.get("type"),
# 		      session_id=event.get("session_id"))
#     print(event_obj.timestamp)


# class Rectangle:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def get_area_rect(self):
#         return self.width * self.height
#
#     def __str__(self):
#         return f'Rectangle: {self.x},{self.y},{self.width},{self.height}'
#
#
# rect1 = Rectangle(5, 10, 50, 100)
# print(rect1)
# print(rect1.get_area_rect())


# class User:
#     def __init__(self,first_name,second_name,city,balance):
#         self.first_name = first_name
#         self.second_name = second_name
#         self.city = city
#         self.balance = balance
#     def get_guests(self):
#         return f' {self.first_name} {self.second_name},г. {self.city}'
#     def get_person(self):
#         return f'{self.first_name} {self.second_name}. {self.city}. Баланс:{self.balance} руб.'
# firstPerson = User("Кирилл","Белов","Анапа",10000000)
# print(firstPerson.get_person())
# guest1 = User("Нарек","Белов","Анапа",50)
# guest2 = User("Ашот","Григорян","Анапа",200)
# guests = [guest1,guest2]
# for guest in guests:
#     print(guest.get_guests())
#
#
