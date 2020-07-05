rows = int(input())

for i in range(rows):
    for j in range(i + 1):
        print(chr(ord('A') + j), end='')
    print()


# print(ord('@'))
# print(chr(122))
# print(chr(13))
# print('hello')
