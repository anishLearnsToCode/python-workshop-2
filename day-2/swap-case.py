def swapCase(string):
    acc = ''
    for character in string:
        acc += character.lower() if character.isupper() else character.upper()
    return acc


print(swapCase(input()))
