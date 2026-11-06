# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         return f"My name is {self.name} and I'm {self.age} years old."

# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)
#         self.breed = breed

#     def fetch(self):
#         print(f"{self.name} is fetching the ball!")


# lucas = Dog("Lucas", "28", "Chihuaha")
# print(lucas.speak())
# lucas.fetch()

# class Vehicle:
#     def __init__(self, brand, speed=10):
#         self.brand = brand
#         self.speed = speed

#     def accelerate(self):
#         print("The car is accelerating!")

# class Bicycle(Vehicle):
#     def __init__(self, brand, speed, has_bell):
#         super().__init__(brand, speed)
#         self.has_bell = has_bell

#     def set_speed(self):
#         self.speed = 10

#     def accelerate(self):
#         print("The bicycle is going faster!")
#         print(f"Your currend speed is {self.speed}")
    
#     def ring_bell(self):
#         if self.has_bell:
#             print("Dring Dring!")
#         else:
#             print("There is no bell on this bicycle")

# my_bicycle = Bicycle("French Bicycle", 10, True)
# my_bicycle.accelerate()
# my_bicycle.ring_bell()


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def describe(self):
#         return f"{self.title} is written by {self.author}."

# class Ebook(Book):
#     def __init__(self, title, author, file_size):
#         super().__init__(title, author)
#         self.file_size = file_size

#     def download(self):
#         return f"Downloading the file. File size: {self.file_size}KB."

# my_book = Ebook("My Book", "Me", 100)
# print(my_book.describe())
# print(my_book.download())


# class Shape:
#     def __init__(self, color):
#         self.color = color

#     def describe(self):
#         print(f"This shape is {self.color}.")

# class Rectangle(Shape):
#     def __init__(self, color, width, height):
#         super().__init__(color)
#         self.width = width
#         self.height = height

#     def area(self):
#         calculated_area = self.width * self.height
#         return calculated_area

# my_rectangle = Rectangle('Red', 10, 20)
# my_rectangle.describe()
# print(my_rectangle.area())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

    def have_birthday(self):
        self.age += 1

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def add_grade(grade):
        grade = grade[grade]
        if grade <= 20:
            return grade
        else:
            return f"Invalid grade: {grade}\nYour grade must be between 0 and 20."

    def average(self):
        