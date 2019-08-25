"""
    First decorators in python 
"""

def introduce():
    print("Hello!")

def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

# Assinging the decorator to the function in an old fashion way
introduce = decorator(introduce)
introduce()

# We can do it in a fancier way
@decorator
def say_goodbye():
    print("Bye bye")

say_goodbye()

# Decorators with arguments
def decorator_with_arguments(func):
    def wrapper(*args, **kwargs):
        print("With arguments")
        func(*args, **kwargs)
    return wrapper


@decorator_with_arguments
def say_personalized_introduction(name, age=20):
    print("My name is: " + name, age)


say_personalized_introduction(age=22, name="Eder")
