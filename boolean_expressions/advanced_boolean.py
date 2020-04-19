"""
In Python you can compare a single element using two binary operators--one on
either side:
"""

x = 3.141
if 3.14 < x < 3.142:
    print("x is near pi")
## x is near pi

"""
In many (most?) programming languages, this would be evaluated in a way contrary
to regular math: (3.14 < x) < 3.142 , but in Python it is treated like
3.14 < x and x < 3.142 , just like most non-programmers would expect.
"""
