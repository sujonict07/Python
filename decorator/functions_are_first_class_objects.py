'''
functions are first class object, that means functions can be passed
around and used as arguments just like any other object(string, int,float, list, and so on)

'''

def say_hello(name):
    # return f"Hello {name}"
    return "Hello {}".format(name)

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def greet_bob(greeter_function):
    return greeter_function("Emon")

print(greet_bob(say_hello))

# output : Hello Emon

print(greet_bob(be_awesome))
# Yo Emon, together we are the awesomest!