# decorators wrap a function, modifying its behavior.


def my_decorator(func):

    def wrapper():
        print("something is happend before the function is called")
        func()
        print("something is happend after the function is called")

    return wrapper


def say_whee():
    print("whee!")


say_whee = my_decorator(say_whee)
print(say_whee)
