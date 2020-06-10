"""
In Python, mangling is used for "private" class members which are
designated as such by giving them a name with two leading underscores
and no more than one trailing underscore. For example, __thing will
be mangled, as will ___thing and __thing_, but __thing__ and
__thing___ will not. Python's runtime does not restrict access to
such members, the mangling only prevents name collisions if a derived
class defines a member with the same name.

On encountering name mangled attributes, Python transforms these names
by prepending a single underscore and the name of the enclosing class:
    _classname__identifier

"""

class Test(object):
    def __mangled_name(self):
        pass
    def normal_name(self):
        pass

t = Test()

print([attr for attr in dir(t) if 'name' in attr])
# ['_Test__mangled_name', 'normal_name']
print("-----------------")
"""
Second example
"""

class Student: 
    def __init__(self, name): 
        self.__name = name 
  
    def displayName(self): 
        print(self.__name) 
  
s1 = Student("Santhosh") 
s1.displayName() 
  
# Raises an error 
try:
    print(s1.__name)
except AttributeError:
    print("'Student' object has no attribute '__name'")
"""
However it is possible to access them anyway
"""
print("{} is an original name".format(s1._Student__name)) 
s1.__Student__name = 'Pawel'    # trying to change the name of student
s1.displayName() # name didn't not changed - still Santhosh

print("-----------------")
"""
Python code to illustrate how mangling works  
With method overriding

This is helpful for letting subclasses override methods without breaking
intraclass method calls.
"""
  
class Map:  
    def __init__(self):  
        self.__geek()  
          
    def geek(self):  
        print("In parent class")  
    
    # private copy of original geek() method is called in init constructor  
    __geek = geek     
    
class MapSubclass(Map):  
        
    # provides new signature for geek() but  
    # does not break __init__()  
    def geek(self):          
        print("In Child class") 
          
# Driver's code 
obj = MapSubclass()
print("xxxxxxx")
obj.geek() 

