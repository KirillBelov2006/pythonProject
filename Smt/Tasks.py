# a = int(input("Введите значение: "))
# b = int(input("Введите второе значение: "))
#
# count = 0
# for i in range(a,b+1):
#     print(i)
#     count+=1
# print("Кол-во чисел:",count)

# a = float(input("Стоимость 1 кг конфет: "))
# cost = 0
# for i in range(1,11):
#     cost+=a
#     print(i,"Кг","Цена",cost)

# a = int(input("Введите кол-во чисел в последовательности: "))
# summa = 0
# for i in range(1,a+1):
#     b = int(input("Введите значение: "))
#     if b < 0:
#         summa=summa+b
# print(summa)

# count = 0
# a = int(input("Введите значение: "))
# if a>0:
#     count+=1
# a = int(input("Введите значение: "))
# if a>0:
#     count+=1
# a = int(input("Введите значение: "))
# if a>0:
#     count+=1
# print(count)

# a = int(input("Введите значение: "))
# if a > 0 :
#     a+=1
# elif a < 0:
#     a-=2
# print(a)

# a = int(input("Введите значение: "))
# q = 0
# while a != 0:
#     if a > 10:
#         q+=1
#     a = int(input("Введите значение: "))
# print(q)

# a = int(input("Введите значение: "))
# q = 0
# while a != 0:
#     if a > 0:
#         q+=a
#     a = int(input("Введите значение: "))
# print(q)

# a = int(input("Введите кол-во чисел в последовательности:"))
# count = 0
# for i in range (0,a):
#     a = int(input("Введите число:"))
#     if a<=30000:
#         if a%6 == 0 and a%10==4:
#             count+=1
# print(count)

# a = int(input("Введите кол-во чисел:"))
# summa = 0
# q = 0
# while a!=0:
#     if a%2 == 0:
#         summa += a
#     q+=1
#     a = int(input("Введите кол-во чисел:"))
# print(q)
# print(summa)




# some_digit = int(input("Введите число: "))
# if some_digit > 0:
#     print("Число положительное")
# else:
#     print("Число отрицательное или равно 0")

# some_str = input("Введите строку: ")
# print(len(some_str))

# some_str = input("Введите строку: ")
# print(some_str[-1])

# some_digit = int(input("Введите число: "))
# if some_digit % 2 == 1:
#     print("Число нечетное")
# else:
#     print("Число четное")

# first_word = input("Введите первое слово: ")
# second_word = input("Введите второе слово: ")
# if first_word[0] == second_word[0]:
#     print("Первые буквы совпадают")
# else:
#     print("Первые буквы не совпадают")


# some_word = input("Введите слово: ")
# if some_word[-1] == "ь":
#     print(some_word[-2])
# elif some_word[-1] != "ь":
#     print(some_word[-1])

# some_number = int(input("Введите значение: "))
# some_number = str(some_number)
# print(some_number[0])
#
# some_number = int(input("Введите значение: "))
# some_number = str(some_number)
# print(some_number[-1])

# some_number = int(input("Введите значение: "))
# some_number = str(some_number)
# first_digit = int(some_number[0])
# last_digit = int(some_number[-1])
# print(first_digit+second_digit)

# some_number = int(input("Введите значение: "))
# some_number = str(some_number)
# print(len(some_number))

#
# first_number = int(input("Введите первое значение: "))
# second_number = int(input("Введите второе значение: "))
#
# first_number = str(first_number)
# second_number = str(second_number)
#
# first_digit = int(first_number[0])
# second_digit = int(second_number[0])
#
# if first_digit == second_digit:
#     print("Первые цифры совпадают")
# else:
#     print("Не совпадают")
#
# some_list = [1,2,3,4,5,6]
# print(some_list[0:3])

# some_stroke = input("Введите значение: ")
# if some_stroke > some_stroke[0]:
#     print(some_stroke[-2])

# first_number = int(input("Введите первое число: "))
# second_number = int(input("Введите второе число: "))
# if first_number%second_number == 0 :
#     print("Число делится без остатка")
# else:
#     print("Делится с остатком")

# some_stroke = "abcde"
# print(list(some_stroke))

# some_list = [1,2,3,4,5,6]
# print(some_list[2:5])


# some_dict = {"year":"2025","month":"12","day":"31"}
# data = f"{some_dict['year']}-{some_dict['month']}-{some_dict['day']}"
# print(data)

# some_dict = {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3,
# 	'd': 4,
# }
# print(set(some_dict.values()))

# some_stroke = input("Введите значение: ")
# position = None
#
# for i, digit in enumerate(some_stroke):
# 	if digit.isdigit():
# 		position = i
# 		break
# if position is not None:
# 	print(f"Первая цифра найдена на позиции: {position}")
# else:
# 	print("Цифры не найдено в строке.")


# num = input('Введите число: ')
# count = 0
# for i in num:
# 	i = int(i)
# 	if i % 2 == 0:
# 		count+=1
# print("Количетсво четных цифр:",count)

# dict1 = {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3,
# 	'd': 4,
# }
# print(list(dict1.keys()))

# input_string = 'abcde'
# result_string = ''
#
# for i in range(len(input_string)):
#     if i % 2 == 1:
#         result_string += input_string[i]
#     else:
#         result_string += input_string[i].upper()
#
# print(result_string)


# some_stroke = "2025-12-31"
# print((tuple(some_stroke.split())))



# some_stroke = "abcdefg"
# some_stroke = some_stroke.replace("c", "")
# some_stroke = some_stroke.replace("f","")
# print(some_stroke)


# some_list = [1,2,3,4,5,6]
# even_digit = sum(some_list[1::2])
# odd_digit = sum(some_list[0::2])
# print(even_digit//odd_digit)


# def a_devider_n(a,n):
#     if a%n == 0:
#         print("Число является делителем числа a")
#     else:
#         print("Не является делителем числа а")
# a_devider_n(12,6)

# import math
# def gepotinusa():
#     first_lenght_kat = float(input("Введите длину первого катета: "))
#     second_lenght_kat = float (input("Введите длину второго катета: "))
#     print(math.sqrt(first_lenght_kat**2+second_lenght_kat**2))
# gepotinusa()


# def pay_to_taxi(distance):
#     base = 4.00
#     add = 0.25
#     return  base+(distance/140)*add
# print(pay_to_taxi(280))

# def all_del_a(a):
#     count = 0
#     for n in range(1, a + 1):
#         if a % n == 0:
#             count += 1
#
#     return print(count)
# all_del_a(4)

# def check_palindrome():
#     slovo = str(input())
#     a = slovo[::-1]
#     if slovo == a :
#         print("yes")
#     else:
#         print("no")
# check_palindrome()

# x = 3
# def function():
#     print(x)
#     return x
#
# print(function())


# def all_del_a(a):
#     count = 0
#     for n in range(1, a + 1):
#         if a % n == 0:
#             count += 1
#
#     return print(count)
# all_del_a(4)

# class Person:
#     def __init__(self,name):
#        self.name = name
#        self.age = 1
#
# tom = Person("Tom")
# tom.age = 37
# print(tom.age)
# print(tom.name)



