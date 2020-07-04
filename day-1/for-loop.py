"""
Range
constructors of range
range(stop)
range(start, stop)
range(start, stop, step)
"""

r = range(0, 10, 3)
print(type(r))
# print(r.start)
# print(r.stop)
# print(r.step)

"""
For Loop
for var in itterable_object:
    code
    code
"""

# for i in r:
#     print(i)

# increment (++) and decrement (--) operator are not present in python and any other functional programming language

# n = int(input())
# for i in range(1, n + 1):
#     print(i)

textMessage = 'hello world'
for character in textMessage:
    print(character, end='**')
