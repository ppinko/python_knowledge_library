"""
The == operator compares the values of both the operands and checks for
value equality. Whereas is operator checks whether both the operands refer
to the same object or not.
"""

# python3 code to  
# illustrate the  
# difference between 
# == and is operator 
# [] is an empty list 

"""
Mutable data types when we create a new variable with the same value
store it in different location, as the value can be changed
"""

list1 = [] 
list2 = [] 
list3=list1 
  
print(list1 == list2) # True
print(list1 is list2) # False
print(list1 is list3) # True
print(id(list1), id(list2), id(list3))

"""
Immutable data types when we create a new variable with the same value
store it in THE SAME different location, as the value CANNOT be changed
(there can be only one memory cell with value 10)
"""

x = 1
y = 1
print(x == y) # True
print(x is y) # True
print(id(x), id(y))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

A = Point(1, 2)
B = Point(1, 2)
C = A

print(A == B) # True
print(A is B) # False
print(A is C) # True
print(id(A), id(B), id(C))
print(type(A), type(B))

"""
Some people use the terms “name” and “binding” to more accurately reflect how
variable names work in Python. When we say a = "super hero powers" , we are
creating an object on the right side of the equal sign, and we are binding the
name a to that object. When there are names on either side of the equal sign
(ex: a = b), we are saying bind the name a to the same object that the name b
is bound to.
"""
