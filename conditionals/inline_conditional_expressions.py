"""
The ternary operator is used for inline conditional expressions. It is best
used in simple, concise operations that are easily read.
"""

n = 5
print("Greater than 2" if n > 2 else "Smaller than or equal to 2")
# Out: 'Greater than 2'

""" Ternary operations can also be nested """

print("Hello" if n > 10 else "Goodbye" if n > 5 else "Good day")
# Out: "Good day"


"""
TRUTH VALUES:

The following values are considered falsey, in that they evaluate to False
when applied to a boolean operator:
 
- None
- False
- 0 , or any numerical value equivalent to zero, for example 0L , 0.0 , 0j
- Empty sequences: '' , "" , () , []
- Empty mappings: {}
- User-defined types where the __bool__ or __len__ methods return 0 or False
"""

