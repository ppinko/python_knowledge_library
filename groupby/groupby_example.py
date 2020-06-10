"""
Briefly: The groupby() function takes two arguments: (1) the data to group and
(2) the function to group it with. 

Make an iterator that returns consecutive keys and groups from the iterable.
The key is a function computing a key value for each element. If not specified
or is None, key defaults to an identity function and returns the element
unchanged. Generally, the iterable needs to already be sorted on the same key
function.

The operation of groupby() is similar to the uniq filter in Unix. It generates
a break or new group every time the value of the key function changes (which
is why it is usually necessary to have sorted the data using the same key
function). That behavior differs from SQL’s GROUP BY which aggregates common
elements regardless of their input order.

The returned group is itself an iterator that shares the underlying iterable
with groupby(). Because the source is shared, when the groupby() object is
advanced, the previous group is no longer visible. So, if that data is needed
later, it should be stored as a list.
"""

import itertools 
  
L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)] 
  
# Key function 
key_func = lambda x: x[0] 
  
for key, group in itertools.groupby(L, key_func): 
    print(key + " :", list(group))

## a : [('a', 1), ('a', 2)]
## b : [('b', 3), ('b', 4)]

print('---------------------------')

a_list = [("Animal", "cat"),    
          ("Bird", "peacock"),
          ("Animal", "dog"),
          ("Bird", "pigeon")] 

''' list should be sorted before applying groupby '''
  
an_iterator = itertools.groupby(a_list, lambda x : x[0]) 
  
for key, group in an_iterator: 
    key_and_group = {key : list(group)} 
    print(key_and_group)

## {'Animal': [('Animal', 'cat')]}
## {'Bird': [('Bird', 'peacock')]}
## {'Animal': [('Animal', 'dog')]}
## {'Bird': [('Bird', 'pigeon')]}

print('---------------------------')

''' using sorted list '''

a_list.sort()
an_iterator = itertools.groupby(a_list, lambda x : x[0]) 
  
for key, group in an_iterator: 
    key_and_group = {key : list(group)} 
    print(key_and_group)

## {'Animal': [('Animal', 'cat'), ('Animal', 'dog')]}
## {'Bird': [('Bird', 'peacock'), ('Bird', 'pigeon')]}

''' Example from Stackoverflow

groups = []
uniquekeys = []
for k, g in itertools.groupby(data, keyfunc):
   groups.append(list(g))    # Store group iterator as a list
   uniquekeys.append(k)


k is the current grouping key, and g is an iterator that you can use to iterate
over the group defined by that grouping key. In other words, the groupby
iterator itself returns iterators.
'''
