from decorator.decorators import do_twice
"""
Returning Values From Decorated Functions

"""

@do_twice
def greet(name):
    print(f"Hello {name}")

print(greet("sujon"))




@do_twice
def return_greating(name):
    print("Creating greading")
    return f"Hi {name}"

hi_emon = return_greating("Emon")

print(hi_emon)