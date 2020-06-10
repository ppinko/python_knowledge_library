"""
Consider the below list comprehension:
"""

def f(x):
    import time
    time.sleep(.1)  # Simulate expensive function
    return x**2

l1 = [f(x) for x in range(1000) if f(x) > 10]
# [16, 25, 36, ...]

"""
This results in two calls to f(x) for 1,000 values of x : one call for
generating the value and the other for checking the if condition. If f(x)
is a particularly expensive operation, this can have significant performance
implications. Worse, if calling f() has side effects, it can have surprising
results.

Instead, you should evaluate the expensive operation only once for each value
of x by generating an intermediate iterable (generator expression) as follows:
"""

l2 = [v for v in (f(x) for x in range(1000)) if v > 10]
# [16, 25, 36, ...]


"""
Another option - In general, a separate generator function is recommended
over a complex one-liner:
"""

def process_prime_numbers(iterable):
    for x in iterable:
        if is_prime(x):
            yield f(x)

l3 = [x for x in process_prime_numbers(range(1000)) if x > 10]
# [11, 13, 17, 19, ...]
