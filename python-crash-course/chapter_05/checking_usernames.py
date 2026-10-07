current_users = ['andreina', 'lucas', 'marie-claire', 'tom', 'claire', 'admin']
new_users = ['paul', 'lucas', 'mathieu', 'pierre', 'tom']

current_users_lower = [user.lower() for user in current_users]


for user in new_users:
    if user in current_users_lower:
        print(f"This username: {user} has already been  taken.")
    else:
        print(f"Welcome, {user} This username is available")