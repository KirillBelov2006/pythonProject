class Cats:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender
    def get_age(self):
        return self.age

class Dog(Cats):
    def get_pet(self):
        return "Имя:"f' {self.get_name()}\n{self.get_age()}'

first_dog = Dog("Мухтар","Man",2)
print(first_dog.get_pet())




