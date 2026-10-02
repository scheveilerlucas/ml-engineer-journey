# 4.10

my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice-cream']

message = "The first three items in the list are :"

print(f'{message} {my_foods[:3]}')

print(f'Three items from the middle of the list are: {my_foods[1:4]}')
print(f'The last three items in the list are : {my_foods[-3:]}')


friend_food = my_foods[:]
my_foods.append('calabrese')
friend_food.append('peperoni')
print("My favorite pizzas are")
for food in my_foods:
    print(f"{food}\n")

for food_friend in friend_food:
    print(food_friend)