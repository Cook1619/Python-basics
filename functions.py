def greet(name):
    print(f"Hello there {name}")


# greet("Matt")
# greet("Billy")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting('Matt')
# print(message)

# This is a optional parameter, and if one isn't supplied we are giving it 1


def increment(number, by=1):
    return number + by


# print(increment(2, 2))

# This * infront of the numbers paramter means you don't know how many
# arguments are going to be passed in, we can pass as any as we want
# In this example we are passing in a tuple, and we can iterate over tupels
# and do some work with them


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
        return total


total = multiply(2, 3, 6, 7, 8)
# print(total)
# We are techincally passing this a dicionary, lets us able to pass a function an 'object' in JS
# def save_user(**user):
#     print(user["id"])


# save_user(id=1, name="John", age=22)

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return 'FizzBuzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    return input


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(7))
