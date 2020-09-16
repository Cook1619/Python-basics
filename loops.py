# for number in range(3):
#     print('Running', number + 1, (number + 1) * '.')

# successful = False

# for number in range(3):
#     print('Attempt')
#     if successful:
#         print('Successful')
#         break
# else:
#     print('Unsuccessful')


# Nested Loops
# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")

# Interable
# for x in [1, 2, 3, 4]:
#     print(x)

# # Were not iterating here, we are evaluating a condition and performing a task while the conditon it met
# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)

print(f"We have {count} even numbers")
