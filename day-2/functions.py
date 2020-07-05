"""
Functions
<= 3 parameters
def func_name(parameter1, parameter2, parameter3 ....)
    code
    code
    code
    return value (not compulsory) / void --> no return value, only do stuff
"""


def hello():
    print('hello')


def helloWorld():
    print('hello world')


def fullName(firstName, lastName):
    print(firstName + ' ' + lastName)


def mod(x):
    # if x < 0:
    #     x = -x
    # return x

    return x if x > 0 else -x

# arguments
# fullName('john', 'doe')
# fullName('anish', 'sachdeva')
# f o g (x) --> f(g(x))
# print(mod(8)) # --> print(8) --> 8 is printed
# print(mod(-4))
# print(mod(0))
# print(mod(-76))

val = mod(int(input())) # --> mod(int(input())) --> mod(int('-23')) --> mod(-23) --> 23 --> assign 23 to val
print(val + 10) # --> print(val + 10) --> print(23 + 10) --> print(33) --> print is called and value is printed
