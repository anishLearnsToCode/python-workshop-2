"""
n
1 + 2 + 3 + 4 + ... + n
"""

# print(int('hello')) # --> 3242342 + 3 --> 3242343

number = int(input())
print(number * (number + 1) / 2)

acc = 0
iter = 1
while iter <= number:
    acc = acc + iter # s(iter - 1) + iter
    iter = iter + 1

print(acc)
