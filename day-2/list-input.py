val = input()
# print(type(val))
# print(val)

numbers = val.split(' ')
# print(type(numbers))
print(numbers)

for index in range(len(numbers)):
    numbers[index] = int(numbers[index])
    print(numbers)
