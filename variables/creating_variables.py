# Possible to assign many variable at once
a, b, _ = 1, 2, 3
print(a, b, _)

# Possible to assign many variable ot the same value at one line
c = d = 1
print('c = ', c, ' d = ', d,)

"""
what's on the left of = is just a name for an object. First you call the int
object with value 2 a , then you change your mind and decide to give the name a to a string object, having value
'New value'. Simple, right?
"""
e = 2
print('e = ', e)

e = "New value"
print('e = ', e)
