"""
Lists
f : N --> value

Dictionary / Hashmap / Map
f : value --> value
(key, value)
key is unique, values may or may not be unique

f(key) --> value
"""

words = {
    'i': 500,
    'am': 300,
    'ball': 300
}

# print(words['i'])
# print(words['ball'])
# words.get('ball') = #wrong
# words['ball'] = 800
# print(words['ball'])
# words['round'] = 65
# print(words['round'])

# print(words)
# del words['am']
# print(words)

# values = words.values()
# print(type(values))
#
# keys = words.keys()
# print(type(keys))
# print(keys)

# pairs = words.items()
# print(type(pairs))
# print(pairs)

# for item in words.items():
#     print("key : " + str(item[0]) + ' | value: ' + str(item[1]))

# for key in words.keys():
#     print(key)

# for value in words.values():
#     print(value)

# del words
# print(words)

# dictionary cant be used as key
person = {
    'firstName': 'john',
    'lastName': 'doe',
    'age': 21,
    1: -3.14,
    'online': False,
    'numbers': [2, 3, 5, 7, 11],
    'complex': {
        'hello': 'world',
        range(5): range(10)
    }
}

# print(person)
# value = person['numbers']
# print(value)
# print(type(value))
# value.append(1000)
# value.remove(2)
# print(value)
# print(person)
# print(person['numbers'][3])

person['new-key'] = 'new-value'
person.update({'new-key': 'new-value-2'})

value = person['complex'][range(5)]
print(value)
# print(person['dsaddsasdsd']) this will give key error --> no key exists
print(person)

print('lastName' in person)

# person.clear()
# print(person)