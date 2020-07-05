position = (10, 2)
print(type(position))
print(position.count(10))

print(position[1])
car1 = ('213123', 'honda', 2019, 5)
car2 = ('99898', 'honda', 1998, 3)

cars = []
cars.append(car1)
cars.append(car2)
print(cars)

for car in cars:
    print(car[2])
