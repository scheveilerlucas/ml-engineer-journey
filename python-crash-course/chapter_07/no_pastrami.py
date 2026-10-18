sandwich_orders = [
    "BLT",
    "Croque-monsieur",
    "Club",
    "Pastrami",
    "Reuben",
    "Pastrami",
    "Jambon-beurre",
    "Banh mi",
    "Pastrami",
    "Grilled cheese",
    "Philly cheesesteak",
    "Caprese",
    "Cubano",
    "Pastrami",
]

print("The deli has run out of pastrami")

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

print(sandwich_orders)