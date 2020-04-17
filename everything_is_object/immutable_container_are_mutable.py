"""
Interesting example showing that mutable object can
contain various data which can change over time
"""

l = [1, 2]
x = 10
t = (x, l)
print('t = ', t, ' id = ', id(t), t.__hash__)
print('x = ', x, ' id = ', id(x))
print('l = ', l, ' id = ', id(l))
print('t[0] = ', t[0], ' id = ', id(t[0]), type(t[0]))
print('t[1] = ', t[1], ' id = ', id(t[1]), type(t[1]))

print("--------------------------------")

l.append(3)
x = 20
print('t = ', t, ' id = ', id(t), t.__hash__)
print('x = ', x, ' id = ', id(x))
print('l = ', l, ' id = ', id(l))
print('t[0] = ', t[0], ' id = ', id(t[0]), type(t[0]))
print('t[1] = ', t[1], ' id = ', id(t[1]), type(t[1]))

print("--------------------------------")

l = [1, 3]
x = 11
      
print('t = ', t, ' id = ', id(t), t.__hash__)
print('x = ', x, ' id = ', id(x))
print('l = ', l, ' id = ', id(l))
print('t[0] = ', t[0], ' id = ', id(t[0]), type(t[0]))
print('t[1] = ', t[1], ' id = ', id(t[1]), type(t[1]))
