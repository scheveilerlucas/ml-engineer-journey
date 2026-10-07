user_names = ['andreina', 'lucas', 'marie-claire', 'tom', 'claire', 'admin']

for user_name in user_names:
    if user_name == "admin":
        print(f"\nHello admin, would you like to see a status report?")
    else:
        print(f"Hello {user_name}, welcome in our website.")


user_names = []

if user_names:
    print("There is users.")
else:
    print("\nThere is no users.")
