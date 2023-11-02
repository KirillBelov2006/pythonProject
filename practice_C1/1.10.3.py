class Clients:
    def __init__(self, first_name, second_name, city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.balance = balance
    def get_client_info(self):
        return f'{self.first_name} {self.second_name}. {self.city}. Баланс: {self.balance} руб'
    def get_guests(self):
        return f'{self.first_name} {self.second_name}. {self.city}'


client_1 = Clients("Иван","Петров","Москва","50")
print(client_1.get_client_info())

client1 = Clients('Иван','Петров','Москва',50)
client2 = Clients('Владимир','Зайцев','Кострома',50)
client3 = Clients('Олеся','Янина','Новосибирск',50)

guest_list = [client1,client2,client3]
for guest in guest_list:
    print(guest.get_guests())
