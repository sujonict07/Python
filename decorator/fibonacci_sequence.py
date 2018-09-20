from decorator.decorators import count_calls


@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num -1) + fibonacci(num -2)

print(fibonacci(10))

print(fibonacci.num_calls)

