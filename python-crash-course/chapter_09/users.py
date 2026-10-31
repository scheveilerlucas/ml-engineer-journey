class User:
    def __init__(self, first_name, last_name, age, localisation ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.localisation = localisation

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name}")
        print(f"We are really happy to see you again!")

    def describe_user(self):
        print("This is the information of your account:")
        print(f"Your name is {self.first_name} {self.last_name}.\nYou are {self.age} years old.\nYou live in {self.localisation}.\n")

lucas = User("Lucas", "Scheveiler", 28, "Paris")
marc = User("Marc", "Lepionniner", 22, "Montpellier")
annabelle = User("Annabelle", "Montaigne", 25, "Nice")
clarice = User("Clarice", "Dumont", 49, "Perpignan")


lucas.greet_user()
lucas.describe_user()

marc.greet_user()
marc.describe_user()

annabelle.greet_user()
annabelle.describe_user()

clarice.greet_user()
clarice.describe_user()