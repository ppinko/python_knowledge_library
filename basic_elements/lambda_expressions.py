"""
Script presenting use and power of lambda expressions.
"""

def identity(x):
	return x + 2 

lambda_identity = lambda x: x + 2

print("Identity of 10 equals {0}".format(identity(10)))
print("Lambda equivalen equals {0}".format(lambda_identity(10)))
print()

################################################################

higher_order_function = lambda x, func: x + func(x)
print(higher_order_function(3, lambda x: x * x))
