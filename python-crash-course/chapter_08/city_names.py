def city_country(city_name, country_name):
    formatted_string = f"{city_name}, {country_name}"
    return formatted_string.title()

print(city_country("Paris", "France"))
print(city_country("london", "UK"))
print(city_country("caracas", "venezuela"))