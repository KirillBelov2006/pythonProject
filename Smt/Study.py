# # st1 = {1, 2, 3}
# # st2 = {4, 5, 6}
# # print(set.union(st1,st2))
#
# # S = 0
# # n = 1
# #
# # while S ** 2  < 1000:
# #     S += n
# # print(S)
# #
# # n = 1
# # while True:  # в данной программе это условие всегда True, цикл будет бесконечным
# #     print("Kirill")
# #     n += 1
# #     if n > 10:
# #         break
# #
# # def n_and_a(a,n):
# #     if a % n == 0:
# #         print("n является делителем числа а")
# #     else:print("n не является делителем числа a")
# # n_and_a(4,2)
# # n_and_a(5,3)
#
#
# # any_number1 = int(input("Введите первое значение: "))
# # any_number2 = int(input("Введите второе значение: "))
# # if any_number1 > any_number2:
# #     print(any_number1,"Больше",any_number2)
# # else:
# #     print(any_number2, "Больше" ,any_number1)
#
# # any_number = int(input("Введите значение: "))
# # if any_number % 2 == 0:
# #     print("Значение чётное")
# # else:
# #     print("Значение нечетное")
#
#
# # a = int(input("Введите первое большее число: "))
# # b = int(input("Введите второе меньшее число: "))
# # c = a % b
# # d = a / b
# # if a%b == 0:
# #     print('Число "а" кратно числу "b".', '\nРезультат деления:', int(d), end='.')
# # else:
# #     print('Число "a" некратно числу "b".\nОстаток от деления:', c, end='.')
#
# # one_l_bottle = int(input("Введите кол-во бутылок 1 литра и меньше: "))
# # more_l_bottle = int(input("Введите кол-во бутылок больше 1 литра: "))
# #
# # small = 0.10
# # large = 0.25
# #
# # refund = one_l_bottle * small + more_l_bottle * large
# # print("Ваша выручка составит $%.2f."% refund)
#
#
# # sum_order = float(input("Введите сумму заказа в ресторане: "))
# #
# # waiter = sum_order * 0.18
# # print("Чаевые официанту = %.2f"%waiter)
# # tax = sum_order * 0.05
# # print("Налог = %.2f"%tax)
# #
# # server_plus_tax = sum_order + waiter + tax
# # print("Чаевые и налог = %.2f"%server_plus_tax)
#
#
# # n = int(input("Введите положительное число: "))
# # summa = n * (n+1) / 2
# # print("Сумма первых", n, "положительных чисел =",summa)
#
# # souvenir_weight = 75
# # some_things_weight = 112
# #
# # souvenirs = int(input("Введите кол-во сувениров: "))
# # some_things = int(input("Введите кол-во безделушек: "))
# #
# # all_weight = souvenir_weight * souvenirs + some_things_weight * some_things
# # print(all_weight,"Вес в граммах")
#
# # colors = 'red green blue'
# # colors_split = colors.split() # список цветов по-отдельности
# # print(colors_split)
# # colors_joined = ' and '.join(colors_split) # объединение строк
# # print(colors_joined)
#
#
# # first_dep = int(input("Введите сумму изначального депозита: "))
# #
# # first_year = 0.04
# # second_year = 0.04 + 0.04
# # third_year = 0.04 + 0.04*2
# #
# # first_percent = first_dep * first_year + first_dep
# # print("Сумма за первый год = %.2f"%first_percent)
# #
# # second_percent = first_dep * second_year + first_dep
# # print("Сумма за второй год = %.2f"%second_percent)
# #
# # third_percent = first_dep * third_year + first_dep
# # print("Сумма за третий год = %.2f"%third_percent)
#
# # import math
# # a = int(input("Введите первое число: "))
# # b = int(input("Введите второе число: "))
# # summa = a + b
# # difference = a - b
# # composition = a * b
# # chastnoe = a / b
# # ostatok = a % b
# # Log = math.log10(a)
# # stepen = a ** b
# # All_operations = summa, difference, composition, chastnoe, ostatok, Log, stepen
# # print(All_operations)
#
#
# # b = float(int(input("Введите длину основания треугольника: ")))
# # h = float(int(input("Введите высоту треугольника: ")))
# #
# # area =  (b * h) / 2
# # print("S треугольника =",area)
#
#
# # any_number = int(input("Введите четырёхзначное число-"))
# # summa = 0
# # while any_number != 0:
# #     p = any_number % 10
# #     summa += p
# #     any_number = any_number // 10
# # print(summa)
#
#
# # any_number = int(input("Введите значение: "))
# # if any_number % 2 == 0:
# #     print("Число чётное")
# # else:
# #     print("Число нечётное")
#
#
# # any_age = int(input("Введите возраст: "))
# # if any_age <= 0:
# #     print("Возраст неверный")
# # elif any_age == 1:
# #     print(10.5)
# # elif any_age == 2:
# #     print(10.5+10.5)
# # else:
# #     print((21+(any_age*4)))
#
#
# # any_letter = input("Введите букву латинского алфавита: ")
# # any_list = ["a","e","i","o" and "u"]
# # if any_letter in any_list:
# #     print("Буква гласная")
# # elif any_letter == "y":
# #     print("Буква может быть гласной или согласной")
# # else:
# #     print("Это буква согласная")
#
# # sides = int(input("Введите кол-во сторон фигуры: "))
# # if sides == 3:
# #     print("Треугольник")
# # elif sides == 4:
# #     print("Четырёхугольник")
# # elif sides == 5:
# #     print("Пятиугольник")
# # elif sides == 6:
# #     print("Шестиугольник")
# # elif sides == 7:
# #     print("Семиугольник")
# # elif sides == 8:
# #     print("Восьмиугольник")
# # elif sides == 9:
# #     print("Девятиугольник")
# # elif sides == 10:
# #     print("Десятиугольник")
# # else:
# #     print("Кол-во сторон не подходит")
#
# # months = int(input("Введите номер месяца:"))
# # if months == 1:
# #     print("в месяце 31 день")
# # elif months == 2:
# #     print("в месяце 28 или 29 дней ")
# # elif months == 3:
# #     print("в месяце 31 день ")
# # elif months == 4:
# #     print("в месяце 30 дней ")
# # elif months == 5:
# #     print("в месяце 31 день ")
# # elif months == 6:
# #     print("в месяце 30 дней")
# # elif months == 7:
# #     print("в месяце 31 день ")
# # elif months == 8:
# #     print("в месяце 31 день ")
# # elif months == 9:
# #     print("в месяце 30 дней")
# # elif months == 10:
# #     print("в месяце 30 дней ")
# # elif months == 11:
# #     print("в месяце 30 дней ")
# # elif months == 12:
# #     print("в месяце 31 день ")
# #
#
#
# # noise = int(input("Введите уровень шума в дБ: "))
# # if noise == 40:
# #     print("Тихая комната")
# # elif noise == 70:
# #     print("Будильник")
# # elif noise == 106:
# #     print("Газовая газонокосилка")
# # elif noise == 130:
# #     print("Отбойный молоток")
# # elif 40<noise<=69:
# #     print("Будильник или Тихая комната")
# # elif 70<noise<=105:
# #     print("Будильник или Газовая газонокосилка")
# # elif 106<noise<=129:
# #     print("Газовая газонокосилка или Отбойный молоток")
# # else:
# #     print("Значение уровня шума вне диапозона")
#
#
# # a = int(input("Введите длину стороны a: "))
# # b = int(input("Введите длину стороны b: "))
# # c = int(input("Введите длину стороны c: "))
# # if a == b == c:
# #     print("Треугольник равносторонний")
# # elif a == b != c or a != b == c or a != c == b or b != c == a:
# #     print("Треугольник равнобедренный")
# # elif a != b != c:
# #     print("Треугольник разносторонний")
#
#
# # x = int(input("Введите целое число (0 для выхода): "))
# # # Запускаем цикл, пока пользователь не введет ноль
# # while x != 0:
# #     if x > 0:
# #         print("Это положительное число.")
# #     else:
# #         print("Это отрицательное число.")
#
#
# # num = float(input("Введите число: "))
# # # Сохраняем подходящее значение в переменной result
# # if num == 0:
# #     result = "Введен ноль"
# # if num != 0:
# #     result = "Введен не ноль"
# # # Отобразим результат
# # print(result)
#
#
# # nominal = str(input("Введите номинал банкноты: "))
# # if nominal =="1$":
# #     print("На банкноте изображен Джордж Вашингтон")
# # elif nominal == "2$":
# #     print("На банкноте изображен Томас Джефферсон")
# # elif nominal == "5$":
# #     print("На банкноте изображен Авраам Линкольн")
# # elif nominal == "10$":
# #     print("На банкноте изображен Александр Гамильтон")
# # elif nominal == "20$":
# #     print("На банкноте изображен Эндрю Джексон")
# # elif nominal == "50$":
# #     print("На банкноте изображен Улисс Грант")
# # elif nominal == "100$":
# #     print("На банкноте изображен Бенджамин Франклин")
# # else:
# #     print("Ошибка")
#
#
# # Month = int(input("Введите месяц: "))
# # Day = int(input("Введите день: "))
# # if Month == 1 and Day == 1:
# #     print("Новый год")
# # elif Month == 7 and Day == 1:
# #     print("День Канады")
# # elif Month == 12 and Day == 25:
# #     print("Рождетсво")
# # else:
# #     print("На эту дату нет праздников")
#
#
# # digit = int(input("Введите цифру на шахматной доске: "))
# # letter = str(input("Введите букву на шахматной доске: "))
# # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# # digits = range(1, 9)
# #
# # if letter not in letters:
# #     print('Not in list, use A-H')
# # elif digit not in digits:
# #     print('Not in list, use 1-8')
# # else:
# #     letter_index = letters.index(letter)
# #     digit_index = digits.index(digit)
# #     if letter_index % 2 == digit_index % 2:
# #         print('Black')
# #     else:
# #         print('White')
#
#
# #
# # a = 0
# # b = 0
# #
# # while id(a) == id(b):
# #     a -= 1
# #     b -= 1
# #
# # print(a)
#
#
# # some_text = input("Введите текст: ")
# # some_text=list(set(some_text))
# #
# # print("Уникальных символов:",len(some_text))
#
#
# # digit = int(input("Введите число: "))
# # if type(digit) == int and digit in range(1,100) and digit % 2 == 0 and digit % 3 == 0:
# #     print("Число подходит")
# # else:
# #     print("Число не подходит")
#
# #
# # stroke = "abcdef"
# # print(stroke[::2])
#
#
# # number = 12345
# # number = str(number)
# # print(number[::-1])
#
# # mas = ['Это просто строка','http://golos.io','Ещё одна строка','http://golosboard.ru']
# # for i in mas:
# #     if i[:4] == 'http':
# #         print(i)
#
# # Month = input("Введите месяц вашего рождения: ")
# # Day = int(input("Введите день вашего рождения: "))
# # if Month == "Декабрь" and 22<=Day<=31 or Month == "Январь" and 1<=Day<=19:
# #     print("Козерог")
# # elif Month == "Январь" and 20<=Day<=31 or Month == "Февраль" and 1<=Day<=18:
# #     print("Водолей")
# # elif Month == "Февраль" and 19<=Day<=29 or Month == "Март" and 1<=Day<=20:
# #     print("Рыбы")
# # elif Month == "Март" and 21<=Day<=31 or Month == "Апрель" and 1<=Day<=19:
# #     print("Овен")
# # elif Month == "Апрель" and 20<=Day<=30 or Month == "Май" and 1<=Day<=20:
# #     print("Телец")
# # elif Month == "Май" and 21<=Day<=31 or Month == "Июнь" and 1<=Day<=20:
# #     print("Близнецы")
# # elif Month == "Июнь" and 21<=Day<=30 or Month == "Июль" and 1<=Day<=22:
# #     print("Рак")
# # elif Month == "Июль" and 23<=Day<=31 or Month == "Август" and 1<=Day<=22:
# #     print("Лев")
# # elif Month == "Август" and 23<=Day<=31 or Month == "Сентябрь" and 1<=Day<=22:
# #     print("Дева")
# # elif Month == "Сентябрь" and 23<=Day<=30 or Month == "Октябрь" and 1<=Day<=22:
# #     print("Весы")
# # elif Month == "Октябрь" and 23<=Day<=31 or Month == "Ноябрь" and 1<=Day<=21:
# #     print("Скорпион")
# # elif Month == "Ноябрь" and 22<=Day<=30 or Month == "Декабрь" and 1<=Day<=21:
# #     print("Стрелец")
#
# # rating_of_employee = float(input("Введите рейтинг сотрудника из таблицы: "))
# # salary = 2400
# # if rating_of_employee == 0.0:
# #     print("Низкий Уровень\nПрибавка к зарплате = 0\nЗарплата = 2400.00")
# # elif rating_of_employee == 0.4:
# #     print("Средний уровень\n""Прибавка к зарплате =",2400.00*0.4,"\nЗарплата =",(2400*0.4) + 2400)
# # elif rating_of_employee == 0.6 or rating_of_employee > 0.6:
# #     print("Высокий уровень\n""Прибавка к зарплате =", 2400.00 * 0.6, "\nЗарплата =", (2400 * 0.6) + 2400)
# # else:
# #     print("Неверное значение")
#
# # for i in range(10, 1000):
# #     digits = [int(digit) for digit in str(i)]
# #     if len(digits) >= 2 and digits[0] + digits[1] == 5:
# #         print(i)
# # x = int(input("Введите значение: "))
# # while x != 0:
# #     if x > 0:
# #         print("Это положительное число.")
# #     else:
# #         print("Это отрицательное число.")
# #
# # x = int(input("Введите целое число (0 для выхода): "))
#
#
# # message = input("Введите сообщение (оставьте его пустым для выхода): ")
# # # Начало цикла, пока сообщение не станет пустым
# # while message != "":
# #     n = int(input("Сколько раз повторить сообщение? "))
# #     for i in range(n):
# #         print(message)
# # # Запрашиваем следующее сообщение
# # message = input("Введите сообщение (оставьте его пустым для выхода): ")
#
#
# # numbers = [-1, 2, -3, 4, -5, 6, -7, 8, -9]
# #
# # positive_numbers = [ i for i in numbers if i > 0]
# #
# # print(positive_numbers)
#
#
# # some_stroke = "Hey,What's your favorite movie?"
# # some_stroke = list(some_stroke)
# # print(sorted(some_stroke[:-2]))
#
# # something = ["Достака","Борщ.html","window.html","block"]
# # for i in something:
# #     if i.endswith("html"):
# #         print(i)
#
#
# # P = 1
# # N = 5
# # for i in range(1, N+1):
# #     print("Значение суммы на предыдущем шаге: ", P)
# #     print("Текущее число: ", i)
# #     P *= i
# #     print("Значение суммы после сложения: ", P)
# #     print("---")
# # print("Конец цикла")
# # print()
# # print("Ответ: сумма равна = ", P)
#
#
# # for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
# #     print("Значение суммы на предыдущем шаге: ", S)
# #     print("Текущее число: ", i)
# #     S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
# #     print("Значение суммы после сложения: ", S)
# #     print("---")
# # print("Конец цикла")
# # print()
# # print("Ответ: сумма равна = ", S)
#
# # N = 5
# #
# # for i in range(1, N + 1):
# #    print("*" * i)
#
# # def print_ladder(n):
# #     if n == 3:
# #         for i in range(n):
# #             i+=1
# #             print("*"*i)
# #     elif n == 4:
# #         for i in range(n):
# #             i+=1
# #             print("*"*i)
# # print_ladder(4)
# # print("Сумма за третий год = %.2f"%third_percent)
#
# # price = [4.95, 9.95, 14.95, 19.95, 24.95]
# # for x in price:
# #     print(x, f'{x*0.6:.{2}f}', f'{x-x*0.6:.{2}f}')
#
# # marks ={ 'A+': 4.0, 'C+': 2.3,
# #     'A':  4.0, 'C':  2.0,
# #     'A-': 3.7, 'C-e': 1.7,
# #     'B+': 3.3, 'D+': 1.3,
# #     'B':  3.0, 'D':  1.0,
# #     'B-': 2.7, 'F':  0
# # }
# # print(marks.get(input('Буквенная оценка: '), 'Неизвестная оценка'))
#
# # lens = int(input("Введите длину волны:"))
# # if 380<=lens<450:
# #     print("Фиолетовый")
# # elif 450<=lens<495:
# #     print("Синий")
# # elif 495<=lens<570:
# #     print("Зеленый")
# # elif 570<=lens<590:
# #     print("Желтый")
# # elif 590<=lens<620:
# #     print("Оранжевый")
# # elif 620<=lens<=750:
# #     print("Красный")
# # else:
# #     print("Неверное значение")
# import datetime
#
# # def print_2_add_2():
# #     print(2+2)
# # print_2_add_2()
# #
# # def hello_world():
# #     print("Hello world")
# # hello_world()
#
# # limit = int(input("Введите целое число: "))
# # # Выводим все числа, кратные трем, вплоть до указанного пользователем значения
# # print("Все числа, кратные трем, вплоть до", limit, ":")
# # for i in range(3, limit + 1, 3):
# #  print(i)
# #
# # %.2f"% %.2f"%server_plus_tax
# # sale = 0.6
# # purchase = [4.95, 9.95,14.95,19.95,24.95]
# # for i in purchase:
# #     print(round(i,2),"Изначальная цена", round(i * 0.6, 2),"Цена со скидкой",round(i-i*0.6,2),"Размер скидки")
# #
# #
# # for i in range(101):
# #     f = int(9/5)*i +32
# #     print(f'C-{i}, F-{f}')
#
# # a = int(input("Первое значение: "))
# # # b = int(input("Второе значение: "))
# # # if a and b < 0:
# # #     print("Ложные переменные")
# # a = int(input("Введите значение"))
# # if all([type(a) == int,
# #         100 <= a <= 999,
# #         a % 2 == 0,
# #         a % 3 == 0]):
# #     print("Число удовлетворяет условиям")
#
# # number = 12345
# # reversed_number = 0
# #
# # while number != 0:
# #     digit = number % 10
# #     reversed_number = reversed_number * 10 + digit
# #     number //= 10
# #
# # print("Перевёрнутое число:", reversed_number)
#
# # digit_list = [1,-4,2,-6,4,6,-11,7,8]
# # for i in digit_list:
# #     if i > 0 :
# #         print(i)
# #
# # some_list = [1.456,2.125,3.32,4.1,5.34]
# # for i in some_list:
# #     print(round(i,1),end=", ")
#
# # some_dict = {"a":1,"b":2,"c":3,"d":4,}
# # print(list(some_dict.values()))
#
# # def check_last_first(word1, word2):
# #     last_char = word1[-1].lower()  # Получаем последнюю букву первого слова (приведенную к нижнему регистру)
# #     first_char = word2[0].lower()  # Получаем первую букву второго слова (приведенную к нижнему регистру)
# #
# #     return last_char == first_char  # Возвращаем True, если буквы совпадают, и False в противном случае
# #
# #
# # # Пример использования функции
# # word1 = "Hello"
# # word2 = "orange"
# # result = check_last_first(word1, word2)
# # print(result)
#
# # def linear_solve(a, b):
# #     if a: # помним, что 0 интерпретируется как False, иначе True
# #         return b / a
# #     elif not a and not b:
# #         return "Бесконечное кол-во корней"
# #     else:
# #         return "Нет корней"
# # edibles = ["отбивные", "пельмени", "яйца", "орехи"]
# # for food in edibles:
# #     if food == "пельмени":
# #         print("Я не ем пельмени!")
# #         break
# #     print("Отлично, вкусные " + food)
# # print("Ужин окончен.")
#
# # some_dict = {"a":1,"b":2,"с":3,"d":4,}
# # print(list(some_dict.keys()))
#
# # a = int(input("Введите значение: "))
# # b = int(input("Введите значение: "))
# # count = 0
# # for i in range(a,b+1):
# #     print(i)
# #     count+=1
# # print("Кол-во чисел",count)
#
# # candies_kg = float(input("Стоимость 1 кг конфет: "))
# # cost = 0
# # for i in range(1,11):
# #     cost=candies_kg*i
# #     print("Стоимость",i,"кг","конфет =",cost)
# # a = int(input("Введите кол-во минут за месяц: "))
# # b = int(input("Введите кол-во сообщений за месяц: "))
# # if a == 50 and b == 50:
# #     print("Оплата за тариф $15,00 ")
# # elif a > 50:
# #     for i in range (a+1):
# #         i= (i*0.25+a)-a
# #         print(i,i)
#
# # class User:
# #     pass
# # peter = User()
# # peter.name = "Peter Robertson"
# #
# # julia = User()
# # julia.name = "Julia Donaldson"
# # print(peter.name)
# # print(julia.name)
# #
# # peter.email = "peterrobertson@mail.com"
# # print(peter.email)
# # print('\n')
# # print(julia.email)
#
# # class User:
# #     pass
# # kirill = User()
# # kirill.name = "Kirill Belov"
# # kirill.email = "kirill.belov2043@mail.ru"
# #
# # liza = User()
# # liza.name = "Liza Kustulidi"
# # liza.email = "liza.kustulidi@mail.ru"
# #
# # print(kirill.name)
# # print(kirill.email)
# # print("\n")
# # print(liza.name)
# # print(liza.email)
#
# # class Product:
# #     def __init__(self,name,category,quantity_in_stock):
# #         self.name = name
# #         self.category = category
# #         self.quantity_in_stock = quantity_in_stock
# #     def is_available(self):
# #         return True if self.quantity_in_stock > 0 else False
#
#
# # some_number = int(input("Введите число: "))
# # if some_number % 2 == 0:
# #     print("Число четное")
# # else:
# #     print("Нечетное")
#
#
# # letter = input("Введите букву латинского алфавита: ")
# # num_lis = list("a","e","i","o","u")
# # if letter == "a" or letter == "e" or letter == "i" or \
# #         letter == "o" or letter == "u":
# #     print("Буква гласная")
# # elif letter == "y":
# #     print("Буква может быть гласной или согласной")
# # else:
# #     print("Введена согласная буква")
#
# # for i in range(5):
# #     print(i+1,end=" " )
# #
# # for i in range(10):
# #     if i % 2 == 0:
# #         print(i  )
#
# # a = 8
# # b = 1
# # while (a>5):
# #     a = a-2
# #     b = b + a
# #     print(b)
#
#
# # colors = 'red green blue'
# # colors_split = colors.split()
# # print(colors_split)
# # colors_joined = ' and '.join(colors_split)
# # print(colors_joined)
#
# # some_number = int(input("Введите диапозон: "))
# # for i in range(some_number):
# #     print(i)
#
# # class User:
# #     pass
# #
# # peter = User()
# # peter.name = "Peter Robertson"
# # peter.email = "peterrobertson@mail.com"
# #
# # julia = User()
# # julia.name = "Julia Donaldson"
# # julia.email = "juliadonaldson@mail.com"
# #
# #
# #
# # print(peter.name,"\n",peter.email,end=" ""\n")
# # print(julia.name,"\n",julia.email)
#
# # class Product:
# #     def __init__(self, name, category, quantity_in_stock):
# #         self.name = name
# #         self.category = category
# #         self.quantity_in_stock = quantity_in_stock
# #
# #     def is_available(self):
# #         return True if self.category == "food" else False
# # eggs = Product("eggs", "food", 5)
# # print(eggs.is_available())
#
#
# # class Event:
# #     def __init__(self, timestamp, event_type, session_id):
# #         self.timestamp = timestamp
# #         self.type = event_type
# #         self.session_id = session_id
# # events = [
# #     {
# #      "timestamp": 1554583508000,
# #      "type": "itemViewEvent",
# #      "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
# #     },
# #     {
# #      "timestamp": 1555296337000,
# #      "type": "itemViewEvent",
# #      "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
# #     },
# #     {
# #      "timestamp": 1549461608000,
# #      "type": "itemBuyEvent",
# #      "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
# #     },
# # ]
# #
# #
# # for event in events:
# #     event_obj = Event(timestamp=event.get("timestamp"),
# # 	              event_type=event.get("type"),
# # 		      session_id=event.get("session_id"))
# #     print(event_obj.type)
#
#
# import datetime
#
#
# # class Product:
# #     max_quantity = 100000
# #
# #     def __init__(self, name, category, quantity_in_stock):
# #         self.name = name
# #         self.category = category
# #         self.quantity_in_stock = quantity_in_stock
# #
# #     def is_available(self):
# #         return True if self.quantity_in_stock > 0 else False
# #
# #
# # class Food(Product):
# #     is_critical = True
# #     needs_to_be_refreshed = True
# #     refresh_frequency = datetime.timedelta(days=1)
# #
# #
# # eggs = Food(name="eggs", category="food", quantity_in_stock=5)
# # print(eggs.max_quantity)
# # print(eggs.is_available())
#
#
# # class Event:
# #     def __init__(self, timestamp, event_type, session_id):
# #         self.timestamp = timestamp
# #         self.type = event_type
# #         self.session_id = session_id
# # events = [
# #     {
# #      "timestamp": 1554583508000,
# #      "type": "itemViewEvent",
# #      "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
# #     },
# #     {
# #      "timestamp": 1555296337000,
# #      "type": "itemViewEvent",
# #      "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
# #     },
# #     {
# #      "timestamp": 1549461608000,
# #      "type": "itemBuyEvent",
# #      "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
# #     },
# # ]
# #
# #
# # for event in events:
# #     event_obj = Event(timestamp=event.get("timestamp"),
# # 	              event_type=event.get("type"),
# # 		      session_id=event.get("session_id"))
# #     print(event_obj.timestamp)
#
#
# # class Rectangle:
# #     def __init__(self, x, y, width, height):
# #         self.x = x
# #         self.y = y
# #         self.width = width
# #         self.height = height
# #
# #     def get_area_rect(self):
# #         return self.width * self.height
# #
# #     def __str__(self):
# #         return f'Rectangle: {self.x},{self.y},{self.width},{self.height}'
# #
# #
# # rect1 = Rectangle(5, 10, 50, 100)
# # print(rect1)
# # print(rect1.get_area_rect())
#
#
# # class User:
# #     def __init__(self,first_name,second_name,city,balance):
# #         self.first_name = first_name
# #         self.second_name = second_name
# #         self.city = city
# #         self.balance = balance
# #     def get_guests(self):
# #         return f' {self.first_name} {self.second_name},г. {self.city}'
# #     def get_person(self):
# #         return f'{self.first_name} {self.second_name}. {self.city}. Баланс:{self.balance} руб.'
# # firstPerson = User("Кирилл","Белов","Анапа",10000000)
# # print(firstPerson.get_person())
# # guest1 = User("Нарек","Белов","Анапа",50)
# # guest2 = User("Ашот","Григорян","Анапа",200)
# # guests = [guest1,guest2]
# # for guest in guests:
# #     print(guest.get_guests())
# #
# #
# # class NonPositiveDigitException(ValueError):
# #     pass
# # class Square:
# #     def __init__(self,a):
# #         if a <= 0:
# #             raise NonPositiveDigitException("Неправильно указана сторона квадрата")
#
#
# # import time
# # print(time.strftime("Today is %B, %X время"))
# # print(time.strftime("Today is %B, %M минут"))
# # print(time.strftime("Today is %B, %x Дата"))
# # print(time.strftime("Today is %B, %m Месяц"))
#
#
# import os
# start_path = os.getcwd()
# os.chdir("..")
# print(os.getcwd())
import array

# import calendar
# print(calendar.month(2023,11))
# some_list = ["hola","bonjour","hey"]
# some_list.append("Nihao")
# print(some_list)


# def p(n):
#     print(n)
#     if n > 0:
#         p(n-1)
#         print(n)
# print(p(5))

#
# def par_checker(string):
#     stack = []  # инициализируем стек
#
#     for s in string:  # читаем строку посимвольно
#         if s == "(":  # если открывающая скобка,
#             stack.append(s)  # добавляем её в стек
#         elif s == ")":
#             # если встретилась закрывающая скобка, то проверяем,
#             # пуст ли стек и является ли верхний элемент открывающей скобкой
#             if len(stack) > 0 and stack[-1] == "(":
#                 stack.pop()  # удаляем из стека
#             else:  # иначе завершаем функцию с False
#                 return False
#     # если стек пустой, то незакрытых скобок не осталось
#     # значит возвращаем True, иначе - False
#     return len(stack) == 0

# a = "f"
# if a == a.lower():
#     print("Символ в нижнем регистре")
# else:
#     print("В высшем регистре")

# d_tuple = ("2025", "12", "31")
#
# d_dict = {"year":d_tuple[0], "month":d_tuple[1], "day":d_tuple[2]}
# print(d_dict)


# def greetings(username, age):
#     print(f"hello {username}")
#     print(f"Your age {age}")
#     print('-'*20)
#
# greetings("Kirill", 17)

# def multiplication_number(num1,num2):
#     print(num1*num2)
# multiplication_number(4,6)


# numbers = [i for i in range(1,10) if i % 2==1]
# print(numbers)

# tpl1 = (1, 2, 3)
# tpl2 = (4, 5, 6)
# tpl3 = tpl1+tpl2
# print(tpl3)


# dct1 = {'a': 1,'b': 2,}
# dct2 = {'c': 3, 'd': 4,}
# dct3 = dct1 | dct2
# print(dct3)
# lst1 = [1,2,3]
# lst2 = [4,5,6]
# lst1.extend(lst2)
# print(lst1)


# list_glob = [1,2,3,4,5,6]
# list_glob2 = list_glob[0:3]
# print(sum(list_glob2))

# list1 = [1,2,3,4,5,6]
# list2 = list1[0:3]
# list3 = list1[3:6]
# print(sum(list2)/sum(list3))


# def p(n):
#     print(n)
#     if n > 0:
#         p(n-1)
#         print(n)
# p(5)


# a = [1,2,3]
# a.append(3-1)
# a.pop()
# print(a)


# G = {
#     "Адмиралтейская": {
#         "Садовая": 4},
#     "Садовая": {
#         "Сенная площадь": 4,
#         "Спасская": 3,
#         "Адмиралтейская": 4,
#         "Звенигородская": 5},
#     "Сенная площадь": {
#         "Садовая": 4,
#         "Спасская": 4},
#     "Спасская": {
#         "Садовая": 3,
#         "Сенная площадь": 4,
#         "Достоевская": 6},
#     "Звенигородская": {
#         "Пушкинская": 3,
#         "Садовая": 5},
#     "Пушкинская": {
#         "Звенигородская": 3,
#         "Владимирская": 4},
#     "Владимирская": {
#         "Достоевская": 3,
#         "Пушкинская": 4},
#     "Достоевская": {
#         "Владимирская": 3,
#         "Спасская": 6}
# }
#
#
#
# D = {k : 100 for k in G.keys()}
# D["Адмиралтейская"] = 0
# U = {k : False for k in G.keys()}
#
# D = {k : 100 for k in G.keys()}  # расстояния
# start_k = 'Адмиралтейская'  # стартовая вершина
# D[start_k] = 0  # расстояние от неё до самой себя равно нулю
# U = {k : False for k in G.keys()}  # флаги просмотра вершин
#
# for _ in range(len(D)):
#     # выбираем среди непросмотренных наименьшее по расстоянию
#     min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])
#
#     for v in G[min_k].keys():  # проходимся по всем смежным вершинам
#         D[v] = min(D[v], D[min_k] + G[min_k][v])  # минимум
#     U[min_k] = True  # просмотренную вершину помечаем
#
# D = {k : 100 for k in G.keys()}  # расстояния
# start_k = 'Адмиралтейская'  # стартовая вершина
# D[start_k] = 0  # расстояние от неё до самой себя равно нулю
# U = {k : False for k in G.keys()}  # флаги просмотра вершин
# P = {k : None for k in G.keys()}  # предки
#
# for _ in range(len(D)):
#     # выбираем среди непросмотренных наименьшее по расстоянию
#     min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])
#
#     for v in G[min_k].keys():  # проходимся по всем смежным вершинам
#          if D[v] > D[min_k] + G[min_k][v]:  # если расстояние от текущей вершины меньше
#             D[v] = D[min_k] + G[min_k][v]  # то фиксируем его
#             P[v] = min_k  # и записываем как предок
#     U[min_k] = True  # просмотренную вершину помечаем
#
# pointer = "Владимирская" # куда должны прийти
# path = [] # список с вершинами пути
# while pointer is not None: # перемещаемся, пока не придём в стартовую точку
#    path.append(pointer)
#    pointer = P[pointer]
#
# path.reverse() # разворачиваем путь
# for v in path:
#     print(v)

# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
#
#     def insert_left(self, next_value):
#         if self.left_child is None:
#             self.left_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.left_child = self.left_child
#             self.left_child = new_child
#         return self
#
#     def insert_right(self, next_value):
#         if self.right_child is None:
#             self.right_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.right_child = self.right_child
#             self.right_child = new_child
#         return self
#
#
#     def post_order(self):
#         if self.left_child is not None:  # если левый потомок существует
#             self.left_child.post_order()  # рекурсивно вызываем функцию
#
#         if self.right_child is not None:  # если правый потомок существует
#             self.right_child.post_order()  # рекурсивно вызываем функцию
#
#         print(self.value)
#
#
#
# node_root = BinaryTree(2).insert_left(7).insert_right(5)
# node_7 = node_root.left_child.insert_left(2).insert_right(6)
# node_6 = node_7.right_child.insert_left(5).insert_right(11)
# node_5 = node_root.right_child.insert_right(9)
# node_9 = node_5.right_child.insert_left(4)
#
# node_root.post_order()


# class Node:  # класс элемента
#     def __init__(self, value=None, next_=None):  # инициализируем
#         self.value = value  # значением
#         self.next = next_  # и ссылкой на следующий элемент
#
#     def __str__(self):
#         return "Node value = " + str(self.value)
#
#
# class LinkedList:  # класс списка
#     def __init__(self):  # инициализируем пустым
#         self.first = None
#         self.last = None
#
#     def clear(self):  # очищаем список
#         self.__init__()
#
#     def __str__(self):  # функция печати
#         R = ''
#
#         pointer = self.first  # берём первый указатель
#         while pointer is not None:  # пока указатель не станет None
#             R += str(pointer.value)  # добавляем значение в строку
#             pointer = pointer.next  # идём дальше по указателю
#             if pointer is not None:  # если он существует, добавляем пробел
#                 R += ' '
#         return R
#
#     def pushleft(self, value):
#         if self.first is None:
#             self.first = Node(value)
#             self.last = self.first
#         else:
#             new_node = Node(value, self.first)
#             self.first = new_node
#
#     def pushright(self, value):
#         if self.first is None:
#             self.first = Node(value)
#             self.last = self.first
#         else:
#             new_node = Node(value)
#             self.last.next = new_node
#             self.last = new_node
#
#     def popleft(self):
#         if self.first is None:  # если список пустой, возвращаем None
#             return None
#         elif self.first == self.last:  # если список содержит только один элемент
#             node = self.first  # сохраняем его
#             self.__init__()  # очищаем
#             return node  # и возвращаем сохранённый элемент
#         else:
#             node = self.first  # сохраняем первый элемент
#             self.first = self.first.next  # меняем указатель на первый элемент
#             return node  # возвращаем сохранённый
#
#     def popright(self):
#         if self.first is None:  # если список пустой, возвращаем None
#             return None
#         elif self.first == self.last:  # если список содержит только один элемент
#             node = self.first  # сохраняем его
#             self.__init__()  # очищаем
#             return node  # и возвращаем сохраненный элемент
#         else:
#             node = self.last  # сохраняем последний
#             pointer = self.first  # создаём указатель
#             while pointer.next is not node:  # пока не найдём предпоследний
#                 pointer = pointer.next
#             pointer.next = None  # обнуляем указатели, чтобы
#             self.last = pointer  # предпоследний стал последним
#             return node  # возвращаем сохранённый
#
#     def __iter__(self):  # объявляем класс как итератор
#         self.current = self.first  # в текущий элемент помещаем первый
#         return self  # возвращаем итератор
#
#     def __next__(self):  # метод перехода
#         if self.current is None:  # если текущий стал последним
#             raise StopIteration  # вызываем исключение
#         else:
#             node = self.current  # сохраняем текущий элемент
#             self.current = self.current.next  # совершаем переход
#             return node  # и возвращаем сохранённый
#
#     def __len__(self):
#         count = 0
#         pointer = self.first
#         while pointer is not None:
#             count += 1
#             pointer = pointer.next
#         return count
#
# LL = LinkedList()
#
# LL.pushright(1)
# LL.pushleft(2)
# LL.pushright(3)
# LL.popright()
# LL.pushleft(4)
# LL.pushright(5)
# LL.popleft()
#
# print(len(LL))

#
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# for i in range(len(array)): # проходим по всему массиву
#
#         idx_min = i # сохраняем индекс предположительно минимального элемента
#         for j in range(i+1, len(array)):
#                 if array[j] < array[idx_min]:
#                         idx_min = j
#         if i != idx_min: # если индекс не совпадает с минимальным, меняем
#                 array[i], array[idx_min] = array[idx_min], array[i]

# count = 0
#
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# for i in range(1, len(array)):
#         x = array[i]
#         idx = i
#         while idx > 0:
#                 count += 1
#                 if (array[idx - 1] <= x):
#                         break
#                 array[idx] = array[idx - 1]
#                 idx -= 1
#         array[idx] = x
#
# print(count)

# is_sort = False
# count = 0
#
# while not is_sort:
#         is_sort = True
#         for i in range(len(array)):
#                 idx_min = i
#                 for j in range(i+1, len(array)):
#                         count += 1
#                         if array[j] < array[idx_min]:
#                                 idx_min = j
#                 if i != idx_min:
#                         array[i], array[idx_min] = array[idx_min], array[i]
#
#
#                         is_sort = False
#                         break
# print(array)
# print(count)

# def info(name,age):
#         return f'Hello my name is {name} and my age is {age}'
# print(info("Kirill",25))

# import math
# pi = round(math.pi,2)
# def get_area_circle(radius):
#         return pi*(radius**2)
# print(get_area_circle(2))
# print(round(math.pi,2))

# def max(a,b):
#         if a > b:

# def sum_list(data):
#         lst = []
#         for i in data:
#                 if i % 2 == 0:
#                         lst.append(i)
#         return lst
#
# print(sum_list([1,2,3,4,5])
# def print_message():
#
#         def say_hello():
#                 print("hello")
#         def say_goodbye():
#                 print('bye')
#         say_hello()
#         say_goodbye()
# print_message()


# some_number = 123789
# some_number = str(some_number)
# print(some_number[1::3])


tup = ('2025','12','31')
tup1 = f'year:{tup [0]}\nmonth:{tup [1]}\nday:{tup [2]}'
print(tup1)


# some_lst = []
# for i in range(0,11):
#     some_lst.append(i)
# print(some_lst)

# def check_cap_lett(string):
#     count = 0
#     for i in string:
#         if i.isupper():
#             count+=1
#             if count > 2:
#                 return False
#     return True
# print (check_cap_lett("dgdgG"))


# some_lst = []
# for i in range(0,101):
#     some_lst.append(i)
# print(some_lst[0::2])


# def check_string(string):
#     count = 0
#     for char in string:
#         if char.isalpha():
#             count+=1
#             if count > 3:
#                 return False
#     return True
#
# string = 'a3f5b78'
# print(check_string(string))


# def get_first_even_digit(number):
#
#     number_str = str(number)
#     for digit in reversed(number_str):
#         if int(digit) % 2 == 0:
#             return  int(digit)
#     return None
#
# number = 12345678995785755
# print(get_first_even_digit(number))

