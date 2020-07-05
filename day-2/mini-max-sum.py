numbers = list(map(int, input().split(' ')))
sumNumbers = sum(numbers)
largest = max(numbers)
smallest = min(numbers)

print(sumNumbers - largest, end=' ')
print(sumNumbers - smallest)
