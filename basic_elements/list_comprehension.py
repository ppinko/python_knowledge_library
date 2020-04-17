vec = [-4, -2, 0, 2, 4]

# create a new list with the values doubled
print([x*2 for x in vec]) # [-8, -4, 0, 4, 8]

# filter the list to exclude negative numbers
print([x for x in vec if x >= 0]) # [0, 2, 4]

# apply a function to all the elements
print([abs(x) for x in vec]) # [4, 2, 0, 2, 4]

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit]) 
# ['banana', 'loganberry', 'passion fruit']

# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# the tuple must be parenthesized, otherwise an error is raised

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

##############################################################

"""Nested List Comprehensions"""

matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12], 
     ]

print([[row[i] for row in matrix] for i in range(4)])
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# Equivalent to the below function
# transposed = []
# for i in range(4):
#      transposed.append([row[i] for row in matrix])

# transposed
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


###############################################################

"""MY EXERCISES"""

# Add two lists

list_A = [1, 2]
list_B = [3, 4]

print([list_A[i] + list_B[i] for i in range(len(list_A))])

# Scalar multipy of a list

scalar = 3
print([scalar * i for i in list_A])

"""
Mamy listę, której jedynym elementem jest lista stringów.
Napisać jednolinijkowiec, który spłaszczy strukturę I zwróci listę 
pozostawi tam jedynie stringi, które nie mają w sobie czegos. ( np 
gdzie nie ma litery ‘a')
"""

list_C = [['maroko', 'olo', 'house', 'python', 'bash']]

print([word for row in list_C for word in row if 'a' in word])

