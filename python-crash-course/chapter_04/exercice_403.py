for number in range(1,21):
    print(number)

million = list(range(1, 1_000_001))
for number in million:
    print(number)

print(min(million))
print(max(million))
print(sum(million))



odd_numbers = list(range( 1, 21, 2))
for number in odd_numbers:
    print(number)

threes = list(range(3, 31, 3))
for three in threes:
    print(three)

cubes = [value**3 for value in range(1, 11)]
for cube in cubes:
    print(cube)