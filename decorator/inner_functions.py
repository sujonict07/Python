"""

It’s possible to define functions inside other functions.
Such functions are called inner functions

"""

def parent():
    print("printing from the parent() function")

    def first_child():
        print("printing from the first_child() function")

    def second_child():
        print("printing from the second_child() function")

    second_child()
    first_child()

a = parent()

print(a)

"""
output : 
printing from the parent() function
printing from the second_child() function
printing from the first_child() function
"""