# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# # language = favorite_languages['sarah'].title()

# # print(f"Sarah's favorite language is {language}")


# # Printing the items
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favourite language is {language.title()}.")

# # Printing the keys
# for name in favorite_languages.keys():
#     print(name.title())

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(f'Hi {name.title()}')

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")


# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")



# #  Looping through a dictionnary in a particular order

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank your for taking the poll.")

# # Priting value

# for language in favorite_languages.values():
#     print(language.title())

# # Set = collection in which each item must be unique

# for language in set(favorite_languages.values()):
#                     print(language.title())

# # NOTE You can build a set directly using braces and separating the elements with commas:
# # >>> languages = {'python', 'rust', 'python', 'c'}
# # >>> languages
# # {'rust', 'python', 'c'}



favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

poll_candidate = [
    'jen',
    'sarah',
    'edward',
    'phil',
    'erin',
]

for person in poll_candidate:
    if person not in favorite_languages:
        print(f"{person.title()} you should take the poll!")

    else:
        print(f"{person.title()}, thanks for taking the poll.")
