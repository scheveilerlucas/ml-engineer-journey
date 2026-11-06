class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name}.")
        print(f"And you can eat {self.cuisine_type} cuisine there.")

    def open_restaurant(self):
        print("This restaurant is open!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Define a new type of restaurant called Ice Cream Stand"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)

ice_cream = IceCreamStand("Apera", "venezuelan", ["Chocolat", "Vanilla", "Orange"])
ice_cream.show_flavors()
ice_cream.describe_restaurant()
ice_cream.open_restaurant()