# Абсолютный путь — это путь, который указывает на одно и то же место в файловой системе, вне зависимости от текущего рабочего каталога или других обстоятельств. Его ещё называют полным.
# "Относительный путь — это путь по отношению к текущему рабочему каталогу пользователя."
import fileinput
import os

# import os
#
# start_path = os.getcwd()
# os.chdir(start_path)
# os.getcwd()
# print(os.getcwd())
#
# os.chdir("..")
# os.getcwd()
# print(os.getcwd())
#
#
# import os
# print(os.listdir())


# f = open('test.txt', 'w', encoding='utf8')
#
# # Запишем в файл строку
# f.write("This is a test string\n")
# f.write("This is a new string\n")
# f.close()
# f = open('test.txt', 'r', encoding='utf8')
# print(f.read(10))
# f.close()
#
# f = open('test.txt', 'a', encoding='utf8')
# sequence = ["other string\n", "123\n", "test test\n"]
# f.writelines(sequence)
# f.close()
#
# f = open('test.txt', 'r', encoding='utf8')
# print(f.readlines())
# f.close()
#
# f = open('test.txt', 'r', encoding='utf8')
#
# print(f.readline())  # This is a test string
# print(f.read(4))  # This
# print(f.readline())  # is a new string
#
# f.close()
import os
# my_file = open('input.txt','r', encoding='utf8')
# my_file.close()