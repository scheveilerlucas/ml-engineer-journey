sandwich_orders = [
    "BLT",
    "Croque-monsieur",
    "Club",
    "Reuben",
    "Jambon-beurre",
    "Banh mi",
    "Grilled cheese",
    "Philly cheesesteak",
    "Caprese",
    "Cubano",
]

finished_sandwiches = []

while sandwich_orders:
    made_sandwich = sandwich_orders.pop(0)
    print(f"I made your {made_sandwich} sandwich.")
    finished_sandwiches.append(made_sandwich)


print("\nAll orders are ready:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")