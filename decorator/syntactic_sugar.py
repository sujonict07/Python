"""
@my_decorator

 is just an easier way of saying

 say_whee = my_decorator(say_whee).

 It’s how you apply a decorator to a function.

"""
def my_decorator(func):

    def wapper():
        print("before call function")
        func()
        print("after call function ")

    return wapper

@my_decorator
def say_whee():
    print("hello")
# say_whee = my_decorator(say_whee)
print(say_whee())

