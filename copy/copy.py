import copy

"""
First possibility for list using list.copy()

list.copy() - return a shallow copy
"""

l1 = [1, 2, [0, 0]]
l2 = l1.copy()
print('l1 = ', l1)      # [1, 2, [0, 0]]
print('l2 = ', l2)      # [1, 2, [0, 0]]

l1[2][0] = 77           # it mutates both lists
print('l1 = ', l1)      # [1, 2, [77, 0]]
print('l2 = ', l2)      # [1, 2, [77, 0]]

print('---------------------------------')

"""
Second possibility for list using module: copy

copy.copy(to_copy) - return a shallow copy

This is a little slower than list() because it has to
find out the datatype of old_list first.
"""


l3 = [1, 2, [0, 0]]
l4 = copy.copy(l3)
print('l3 = ', l3)      # [1, 2, [0, 0]]
print('l4 = ', l4)      # [1, 2, [0, 0]]

l3[2][0] = 77           # it mutates both lists
print('l3 = ', l3)      # [1, 2, [77, 0]]
print('l4 = ', l4)      # [1, 2, [77, 0]]

print('---------------------------------')

"""
Third possibility for list using module: copy

copy.deepcopy(to_copy) - return a deep copy

Obviously the slowest and most memory-needing
method, but sometimes unavoidable.
"""

l5 = [1, 2, [0, 0]]
l6 = copy.deepcopy(l5)
print('l5 = ', l5)      # [1, 2, [0, 0]]
print('l6 = ', l6)      # [1, 2, [0, 0]]

l5[2][0] = 77           # it mutates only first list
print('l5 = ', l5)      # [1, 2, [77, 0]]
print('l6 = ', l6)      # [1, 2, [0, 0]]

print('---------------------------------')