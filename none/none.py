"""
None : A singleton object used to signal that a value is absent.

None doesn't have any natural ordering. Using ordering comparison operators
( < , <= , >= , > ) isn't supported anymore and will raise a TypeError.
"""

a = None # No value will be assigned. Any valid datatype can be assigned later

b = 5

##print(b > a) # TypeError

if a is None:
    print("To compare value to None use 'is'")
    
