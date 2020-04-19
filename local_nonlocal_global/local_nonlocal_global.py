"""
nonlocal - keyword adds a scope override to the inner scope.
"""

def counter():
    num = 0
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer

c = counter()
print(c())      # = 1
print(c())      # = 2
print(c())      # = 3

print('-------------------------')

"""
global - keyword means that assignments will happen at the module's top
level, not at the program's top level.

Possible to use 'global' parameters by inner function

In Python, variables inside functions are considered local if and only if they
appear in the left side of an assignment statement, or some other binding
occurrence; otherwise such a binding is looked up in enclosing functions, up to
the global scope.
"""

x = 'Hi'
def read_x():
    print(x)
read_x()        # = Hi

print('-------------------------')

x = 'Hi'
def change_global_x():
    global x
    x = 'Bye'
    print(x)

print(x)            # = Hi
change_global_x()   # = Bye
print(x)            # = Bye

print('-------------------------')

def test():
    def square():
        x = 10
    def rect():
        nonlocal x
        x = 20
    def glo():
        global x
        x = 30
    x = 0
    print(x)    # = 0
    square()
    print(x)    # = 0
    rect()
    print(x)    # = 20
    glo()
    print(x)    # = 20

test()
print(x)        # = 30
