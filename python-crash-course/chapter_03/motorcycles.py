motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append("ducati")
print(motorcycles)

# build lists dynamically
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

# Inserting Elements into a List
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(1, "ducati")
print(motorcycles)

# Deleting Elements

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# Removing an Item Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Finding the Length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)