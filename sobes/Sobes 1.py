def work():
    age = input("Введите ваш возраст: ")
    if not age.isnumeric():
        print("Некорректные данные")
        raise ValueError

    age = int(age)
    if not 0<age<=150:
        print("Некорректные данные")
        raise ValueError
    elif age >= 18:
        print("Вы прошли проверку возраста")
    elif age < 18:
        print("Вы не прошли проверку возраста")

    return None




if __name__=="__main__":
    work()