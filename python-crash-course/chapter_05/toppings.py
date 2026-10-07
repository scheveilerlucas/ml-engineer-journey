requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_topping

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else: 
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")


requested_topping = []

if requested_topping:
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}.')

    print("\n Finished making your pizza!")
else:
    print("\nAre you sure you want a plain pizza?")



available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese'] 
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, We don't have {requested_topping}.")

print("\nFinished making your pizza!")