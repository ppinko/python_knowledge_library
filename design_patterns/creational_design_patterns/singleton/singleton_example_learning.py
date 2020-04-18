"""
Singleton design pattern

Description:

- It guarantees that the given class will have only one instance of the object
and provides a global access point to this instance

- All objects using a given class use the same copy

Usage:

- to manage a shared resource, to avoid conflicting request for the same
resource:
    - a printer spooler
    - a database connection
    - a file manager

Participants:

- The Instance () operation allows the client to get to the only instance of
the class (uniqueInstance)

- Instance () is a static method

- Singleton can be responsible for creating your own unique instance

"""

class Singleton:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance 

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            print("Raised")
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

# A little testing

s = Singleton() # Ok
# s2 = Singleton() # will raise exception
print(s)

s = Singleton.getInstance()
print(s)

s = Singleton.getInstance()
print(s) # will print the same instance as before
