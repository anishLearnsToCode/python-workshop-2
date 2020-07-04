"""
Structure of if else

if predicate:
    code
    code
    code
elif predicate2: (not cumpolsory)
    code
    code
elif predicate3: (not cumpolsory)
    code
    code
elif predicate4: (not cumpolsory)
    code
    code
else: (not compulsory)
    code
    code

elif --> else if
"""

# if 1 > 2:
#     print('i am in if block')
# else:
#     print('i am in else block')
#
# print('i am outside if else')

number = int(input())

if number < 5:
    print('less than 5')
elif 5 <= number < 10:
    print('greater than equal to 5 and less than 10')
elif 10 <= number < 20:
    print('very large number')
else:
    print('OMG!!!!')

print('outside if else block')
