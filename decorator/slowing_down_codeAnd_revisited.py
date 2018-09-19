import functools
import time

def slow_down(_func=None, *, rate=1):
    def decorator_slow_down(func):

        @functools.wraps(func)
        def wapper_slow_down(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wapper_slow_down

    if _func is None:
        return decorator_slow_down
    else:
        return decorator_slow_down(_func)


@slow_down()
def countdown(from_number):
    if from_number < 1:
        print("lol")
    else:
        print(from_number)
        countdown(from_number -1)

print(countdown(3))