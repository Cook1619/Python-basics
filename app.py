import math

print('Hello World')

2 + 3

x = 1

print(x)

name = 'Mathew Cook'

print(len(name))

print(name[0])

print(name[:])

firstName = "Mathew"
lastName = "Cook"
fullName = f"{firstName} {lastName}"

print(firstName.upper())

math.ceil(3.2)

# x = input("x: ")
# print(type(x))
# y = int(x) + 1
# print(f"x: {x}, y: {y}")


# Falsey
# ""
# 0
# None

# everything else is true

temp = 19

if temp > 30:
    print('ITS TRUE')
elif temp > 20:
    print('Its a little cooler')
else:
    print('Its cold')
print('Done')


# age = 12

# message = "Eligible" if age >= 18 else "Not Eligible"
# print(message)

high_income = False
good_credit = True
student = True
if (high_income and good_credit) and not student:
    print('You\'re approved')
else:
    print('Not approved')

for number in range(3):
    print('Running', number + 1, (number + 1) * '.')
