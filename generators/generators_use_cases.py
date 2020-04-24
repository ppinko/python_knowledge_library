"""
Generator expressions are lazily evaluated, which means that they generate and
return each value only when the generator is iterated. This is often useful when
ITERATING THROUGH LARGE DATEBASES, avoiding the need to create a duplicate of
the dataset in memory.
"""

for square in (x**2 for x in range(100)):
    print(square)


"""
Another common use case is to avoid iterating over an entire iterable if doing
so is not necessary.
"""
