rivers = {"nile": "egypt", "amazonas": "venezuela", "han": "korea"}

for river, country in rivers.items():
    print(f"The {river.title()} runs throught {country.title()}")

print()

for river in rivers.keys():
    print(river.title())

print()

for country in rivers.values():
    print(country.title())

