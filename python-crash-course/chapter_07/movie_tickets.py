prompt = "\nHow old are you? (Enter 'quit' to stop) "

while True:
    answer = input(prompt)
    if answer == 'quit':
        break

    age = int(answer)
    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")