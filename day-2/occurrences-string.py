def frequency(string, character):
    count = 0
    for char in string:
        if char == character:
            count += 1
    return count


val = frequency(input(), 'a')
print(val)
