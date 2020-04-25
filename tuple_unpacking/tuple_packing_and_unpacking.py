""" tuple packing """
a = (1, 2, 3) # a is the tuple (1, 2, 3)

""" tuple unpacking """
x, y, z = a
# x == 1
# y == 2
# z == 3

a = 1, 2, 3, 4
_, x, y, _ = a # '_' placeholder for unneeded variables
# x == 2
# y == 3

first, *more, last = (1, 2, 3, 4, 5)
# first == 1
# more == [2, 3, 4] # interesting
# last == 5