from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 8 <= datetime.now().hour <22:
            func()
        else:
            pass

    return wrapper

def say_whee():
    print("whee !")


say_whee = not_during_the_night(say_whee)
print(say_whee())
