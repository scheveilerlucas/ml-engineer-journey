dream_vacation_poll = {}

poll_activated = True



while poll_activated:
    name = input("What's your name? ")
    destination = input("If you could visit one place in the world; where would you go? ")
    dream_vacation_poll[name] = destination

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == "no":
        poll_activated = False

for name, destination in dream_vacation_poll.items():
    print(f"{name.title()} would like to go to {destination.title()}")
    