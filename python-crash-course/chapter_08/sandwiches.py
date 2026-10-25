def list_ingredients(*ingredients):
    print("\nVoici les ingrédients:")
    for ingredient in ingredients:
        print(f"-- {ingredient} --")


list_ingredients("Ham")
list_ingredients("Bread", "Cheese", "Tomato")
list_ingredients("Bread", "Cheese", "Tomato", "Ham")