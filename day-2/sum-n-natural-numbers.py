def sumNNaturalNumbers(n):
    acc = 0
    for i in range(1, n + 1):
        acc += i
    return acc


def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


def permutation(n, r): # nPr --> n! / (n - r)!
    if r < 0 or r > n:
        print('err r should not be greater than n')
        return -1
    return factorial(n) // factorial(n - r)


def combination(n, r): # nCr --> nPr / r!
    if r < 0 or r > n:
        print('err r should not be greater than n')
        return -1
    return permutation(n, r) // factorial(r)


# print(sumNNaturalNumbers(4))
# print(sumNNaturalNumbers(10))
# print(sumNNaturalNumbers(3))
# print(factorial(4))

# print(permutation(3, 0))
# print(permutation(3, 1))
# print(permutation(3, 2))
# print(permutation(3, 3))
# print(permutation(3, -2))

print(combination(4, 0))
print(combination(4, 1))
print(combination(4, 2))
print(combination(4, 3))
print(combination(4, 4))