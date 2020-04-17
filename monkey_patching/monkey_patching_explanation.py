class MyClass:
    a = 1
    b = '2'

##var1 = MyClass()
##var2 = var1
##
##var1.a = 2
##var1.b = '3'
##
##print(var2.a)
### 2
##print(var2.b)
### '3'
##
##print(var1 is var2)

"""
If we go line by line, you see that we create an object using MyClass and we call
it var1. We then copy the object to another variable, called var2. We change the
values stored in var1, but we observe that the values stored in var2 have also
changed. This is simply because, in Python, the variable is only a label. In the
line var2 = var1 we have just copied the label, but both are pointing to the same
underlying object.
"""
var1 = MyClass()
var2 = MyClass()
print(var1.a)
#1
MyClass.a = 2
print(var1.a)
# 2
print(var2.a)
# 2

"""
What we see is that if we directly alter the value of any of the attributes of
the class, the instances inherit this change. This is both very useful and very
dangerous, since you may be altering the value of attributes of objects which
you were not intending to modify.
"""

##var1 = MyClass()
##var2 = var1
##
##var1.a = 2
##var1.b = '3'
##
##MyClass.a = 3
##
##print(var1.a)
### 2
##print(var2.a)
### 2

"""
Even if you change the attribute a to 3, you don't see this change appearing on
the instances of the class. The root cause of this lays in the ideas behind
mutable and immutable data types in Python. Since you altered the value of var1.a,
now the attribute is pointing to an object different from the object the class
attribute points to. If this last line doesn't make sense, go to the articles l
inked earlier on mutable and immutable data types.
"""
