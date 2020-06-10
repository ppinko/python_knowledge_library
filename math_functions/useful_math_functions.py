"""
Collection of useful math functions
"""

import math

print('abs(-5) = ', abs(-5)) # 5

print('pow(2, 3) = ', pow(2, 3)) # 8

# math.sqrt returns FLOAT !!!
print('math.sqrt(100) =', math.sqrt(100)) # 10.0

print('math.exp(1) =', math.exp(1)) # ~2.72

""" trigonometric functions take radians as input
    Similary to sin, there is cos, tan, ctan etc.
"""
print('sin(30deg) =', round(math.sin(math.pi / 6), 2)) # 0.5


""" returns the Euclidean norm, same as math.sqrt(a*a + b*b) """
a, b = 3, 4
print('math.hypot(3, 4) =', math.hypot(a, b)) # 5.0


""" To convert from radians -> degrees and degrees -> radians
respectively use math.degrees and math.radians """
print('math.degrees(math.pi) = ', math.degrees(math.pi)) # 180
print('math.radians(90) = ', math.radians(90)) # 1.57

""" By default, the math.log function calculates the logarithm
of a number, base e. You can optionally specify a base as
the second argument. """

print('math.log(5) =', math.log(5)) # ~1.61
print('math.log(100, 10) =', math.log(100, 10)) # 2.0

""" to find the result of integer division and modulus, you
can use the divmod function as a shortcut """
quotient, remainder = divmod(9, 4)
print('divmod(9, 4) =', quotient, remainder) # (2, 1)
