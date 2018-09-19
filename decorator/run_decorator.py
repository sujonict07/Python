from decorator.decorators import do_twice


@do_twice
def say_whee():
    print("whee!!")

print(say_whee())

