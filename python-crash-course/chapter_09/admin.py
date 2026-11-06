class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name}")
        print(f"We are really happy to see you again!")

    def describe_user(self):
        print("This is the information of your account:")
        print(f"Your name is {self.first_name} {self.last_name}.\nYou are {self.age} years old.\nYou live in {self.location}.\n")

    def increment_login_attempts(self):
        self.login_attempts += 1
        return f"You have logged in {self.login_attempts} times.\n"

    def reset_login_attempts(self):
        self.login_attempts = 0
        return f"Login attempts reset.\nLogin attempts: {self.login_attempts}\n"

class Admin(User):
    def __init__(self, first_name, last_name, age, location):