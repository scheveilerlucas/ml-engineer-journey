class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name}.")
        print(f"And you can eat {self.cuisine_type} cuisine there.")

    def open_restaurant(self):
        print("This restaurant is open!")

my_restaurant = Restaurant('Arepita', 'Venezuelan')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()