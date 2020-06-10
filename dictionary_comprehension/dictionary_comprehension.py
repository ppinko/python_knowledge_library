"""
Example of dict comprehension - possible to use conditionals
"""

print({name: len(name) for name in ('Stack', 'Overflow', 'Exchange') if len(name) > 6})
print('------------------')

"""
Ways of switching key and value of dictionary (invert dictionary)
"""

my_dict = {1: 'a', 2: 'b', 3: 'c'}

## 1) using dict comprehension
swapped_1 = {v: k for k, v in my_dict.items()}      
## 2) using zip function
swapped_2 = dict(zip(my_dict.values(), my_dict))
## 3) using zip function
swapped_3 = dict(zip(my_dict.values(), my_dict.keys()))
## 4) using map and reversed
swapped_4 = dict(map(reversed, my_dict.items()))

print(swapped_1)
print(swapped_2)
print(swapped_3)
print(swapped_4)
print('------------------')

""" Merging dictionaries """

## 1) using dict comprehension
dict1 = {'w': 1, 'x': 1}
dict2 = {'x': 2, 'y': 2, 'z': 2}
print({k: v for d in [dict1, dict2] for k, v in d.items()})
## 2) dict unpacking
print({**dict1, **dict2})
# Out: {'w': 1, 'x': 2, 'y': 2, 'z': 2}
print('------------------')


