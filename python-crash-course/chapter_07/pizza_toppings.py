active = True
user_input = ""
while active:
    if user_input == "quit":
        active = False
    else:
        user_input = input("\nWhat topping would you like? ")
    print(f"\nAdding {user_input} on the pizza!")