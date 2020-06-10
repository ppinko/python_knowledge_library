"""
None - A function that reaches the end of execution without a return statement
will always return None.
"""

def do_nothing():
    pass
print(do_nothing()) # Out: None

"""
Defining a function with an arbitrary number of arguments 
"""

def func(*args):
    # args will be a tuple containing all values that are passed in
    for i in args:
        print(i)

func(1, 2, 3)
# Calling it with 3 arguments
# Out: 1
# 2
# 3

list_of_arg_values = [1, 2, 3]
func(*list_of_arg_values) # Calling it with list of values, * expands the list
# These arguments ( *list_of_arg_values) can be accessed by index, for example
# list_of_arg_values[0] will return the first argument


"""
Defining a function with an arbitrary number of keyword arguments 
"""

def func(**kwargs):
    # kwargs will be a dictionary containing the names as keys and the values as values.
    # kwargs is a plain native python dictionary.
    for name, value in kwargs.items():
        print(name, value)

func(value1=1, value2=2, value3=3) # Calling it with 3 arguments
# Out: value1 1
# value2 2
# value3 3

my_dict = {'foo': 1, 'bar': 2} # Calling it with a dictionary
func(**my_dict)
# Out: foo 1
# bar 2

"""
The order of positional and keywords arguments matters:

- The positional/keyword arguments come first. (Required arguments).
- Then comes the arbitrary *arg arguments. (Optional).
- Then keyword-only arguments come next. (Required).
- Finally the arbitrary keyword **kwargs come. (Optional).
"""

#       |-positional-|-optional-|---keyword-only--|-optional-|
def func(arg1, arg2=10 , *args, kwarg1, kwarg2=2, **kwargs):
    pass

"""
In Python 3, you can use * alone to indicate that all subsequent
arguments must be specified as keywords. For instance the math.isclose
function in Python 3.5 and higher is defined using def math.isclose (a, b,
*, rel_tol=1e-09, abs_tol=0.0) , which means the first two arguments can be
supplied positionally but the optional third and fourth parameters can only
be supplied as keyword arguments.
"""