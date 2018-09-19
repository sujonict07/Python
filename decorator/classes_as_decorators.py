import functools


class Counter:
    def __init__(self, start=0):
        self.count = start


    def __call__(self):
        """
        The .__call__() method is executed each time you
        try to call an instance of the class:
        :return:
        """
        self.count += 1
        print(f"Current count is {self.count}")


counter = Counter()

print(counter())
print(counter())
print(counter())

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls +=1
        print(f"Call {self.num_calls} of {self.func.__name__}!r")
        return self.func(*args, **kwargs)

@CountCalls
def say_whee():
    print("whee")

print(say_whee())
print(say_whee())
print(say_whee())
print(say_whee())