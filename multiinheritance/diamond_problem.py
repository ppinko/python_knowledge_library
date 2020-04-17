"""
            DIAMOND PROBLEM
"""


"""
Example 1 - classical case
"""

class A:
    def say(self):
        print("Class A")

class B(A):
    def say(self):
        print("Class B")

class C(A):
    def say(self):
        print("Class C")

class D(C, B): # mro - first look in C, than in B, than in A and finally 'object'
    def noth(self):
        print("Nothing")

d = D()
d.say()     # "Class C"
print(D.__mro__)
print("-----------------")

"""
Example 2 - Class C inherits method say() from A without overriding
"""

class A:
    def say(self):
        print("Class A")

class B(A):
    def say(self):
        print("Class B")

class C(A):
    def speak(self):
        print("Nevermind")

class D(C, B):
    def noth(self):
        print("Nothing")

d = D()
d.say()     # "Class B" even though class C inherits mathod say from class A
            # it is not directly overriden in C, so it looks in B 
print(D.__mro__)
print("-----------------")

"""
Example 3 - https://en.wikipedia.org/wiki/C3_linearization
"""

class Type(type):
    def __repr__(cls):
        return cls.__name__

class O(object, metaclass=Type): pass


class A(O): pass

class B(O): pass

class C(O): pass

class D(O): pass

class E(O): pass

class K1(A, B, C): pass

class K2(D, B, E): pass

class K3(D, A): pass

class Z(K1, K2, K3): pass

print(Z.mro())
print(Z.__mro__)

"""
Example 4 - deliberatly creating an error
"""

class Type(type):
    def __repr__(cls):
        return cls.__name__

class O(object, metaclass=Type): pass


class A(O): pass

class B(O): pass

class C(O): pass

class D(O): pass

class E(O): pass

class K1(A, B, C): pass

class K2(B, D, E): pass

class K3(D, A, C): pass

class Z(K1, K2, K3): pass

print(Z.mro())
print(Z.__mro__)

"""
Traceback (most recent call last):
  File "/home/devlx/all/python/test_concepts/multiinheritance/diamond_problem.py", line 116, in <module>
    class Z(K1, K2, K3): pass
TypeError: Cannot create a consistent method resolution
order (MRO) for bases A, B, D
"""
