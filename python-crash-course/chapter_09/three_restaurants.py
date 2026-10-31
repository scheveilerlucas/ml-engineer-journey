class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cuisine_type

    def describe_restaurant(self):
        print(f"This is {self.restaurant_name} and you can eat {self.cusine_type} food here!")

    def open_restaurant(self):
        print("The restaurant is open!")


pizza_restaurant = Restaurant("Pizza Place", "italian")
chinese_restaurant = Restaurant("China Wok", "chinese")
venezuelan_restaurant = Restaurant("Arepita", "venezuelan")

pizza_restaurant.describe_restaurant()
chinese_restaurant.describe_restaurant()
venezuelan_restaurant.describe_restaurant()