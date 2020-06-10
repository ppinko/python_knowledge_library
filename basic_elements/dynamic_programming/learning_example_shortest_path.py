""" 
Count all possible path from left top corner of a matrix to right botom corner 
of the matrix


A = [ 
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 'x', 0, 0, 0, 'x', 0],
    [0, 0, 0, 0, 'x', 0, 0, 0],
    ['x', 0, 'x', 0, 0, 'x', 0, 0],
    [0, 0, 'x', 0, 0, 0, 0, 0],
    [0, 0, 0, 'x', 'x', 0, 'x', 0],
    [0, 'x', 0, 0, 0, 'x', 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
"""

A = [ 
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 'x', 0, 0, 0, 'x', 0],
    [0, 0, 0, 0, 'x', 0, 0, 0],
    ['x', 0, 'x', 0, 0, 'x', 0, 0],
    [0, 0, 'x', 0, 0, 0, 0, 0],
    [0, 0, 0, 'x', 'x', 0, 'x', 0],
    [0, 'x', 0, 0, 0, 'x', 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# NAIVE RECURIOSN

# def path(array):
#     i, j = 0, 0
#     return rec_path(array, i, j)

# def rec_path(array, i, j):
#     if i == len(array) - 1 and j == len(array) - 1:
#         return 1
#     elif array[i][j] == 'x':
#         return 0
#     elif i == len(array) - 1:
#         return rec_path(array, i, j+1)
#     elif j == len(array) - 1:
#         return rec_path(array, i+1, j)
#     else:
#         return rec_path(array, i+1, j) + rec_path(array, i, j+1)

# print(path(A))

# MEMOIZED SOLUTION

def path(array):
    i, j = 0, 0
    memo = {}
    return rec_path(array, i, j, memo)

def rec_path(array, i, j, memo):
    if (i,j) in memo:
        return memo[(i,j)]
    if i == len(array) - 1 and j == len(array) - 1:
        to_return = 1
    elif array[i][j] == 'x':
        to_return = 0
    elif i == len(array) - 1:
        to_return = rec_path(array, i, j+1, memo)
    elif j == len(array) - 1:
        to_return = rec_path(array, i+1, j, memo)
    else:
        to_return = rec_path(array, i+1, j, memo) + rec_path(array, i, j+1, memo)
    memo[(i,j)] = to_return
    return to_return

print(path(A))

# DYNAMIC PROGRAMMING SOLUTION

def path(array):
    memo = array[:]
    i = len(array) - 1
    j = i
    while i < 0:
        while j < 0
            if i == len(array) - 1 and j == len(array) -1:
                memo[i][j] = 1
            elif i == len(array) - 1:
                



print(path(A))