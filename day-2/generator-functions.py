"""
Generator Functions
{n | n is a natural number}
{n ^ 2 | n is eal number}
{x + 5 | 4 <= x < 10}

[ f(x, y, ....) for i in itterable ]
brackets decide what you generate
"""

squares = [i ** 2 for i in range(1, 11)]
print(squares)


def swapCase(string):
    return ' '.join([character.lower() if character.isupper() else character.upper() for character in string])


print(swapCase(input()))
