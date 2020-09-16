def greet(name):
    print(f"Hello there {name}")


greet("Matt")
greet("Billy")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting('Matt')
print(message)
