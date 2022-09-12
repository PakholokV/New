class Restaurant:
    def __init__(self,restaurant_name,cuisine_type,):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def descride_restaurant(self):
        print(f"The name of the Restaurant {self.name}, type of kitchen {self.type}")

    def open_restauant(self):
        print(f"The Restaurant {self.name} is Open")

    def client(self):
        print(f"Visitors in the restaurant {self.number_served}")

    def increment_number_served(self, clients):
        self.number_served = clients
        self.clients = 55

    def inc_serv(self,clients):
        self.number_served =+ clients


my_restaurant = Restaurant('Ukraine','Ukrainian')
my_restaurant.descride_restaurant()


my_restaurant.inc_serv(32)
my_restaurant.number_served

my_restaurant.increment_number_served(33)
my_restaurant.number_served