"""
HOW TO SORT IN PYTHON

https://docs.python.org/3/howto/sorting.html

Sorts are guaranteed to be stable. That means that when multiple
records have the same key, their original order is preserved.
"""

"""
1st option using sorted()
- sorted work for any iterable (including string)
- it return list
"""
print('1st option using sorted()')
print(sorted("This is a test string from Andrew".split(), key=str.lower))
# ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']

print('-----------------------')

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
# using lambda function
print(sorted(student_tuples, key=lambda student: student[2]))   # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

print('-----------------------')

class Student:

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),

]

print(sorted(student_objects, key=lambda student: student.age))   # sort by age
#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

print('-----------------------')

"""
2nd option using module operator: itemgetter(), attgetter(), methodcaller()
- allow multiple level of sorting
"""

from operator import itemgetter, attrgetter

print('2nd option using module operator: itemgetter(), attgetter(), methodcaller()')
print(sorted(student_tuples, key=itemgetter(2)))
#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

print(sorted(student_objects, key=attrgetter('age')))
#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

""" Multiple sorting """

print('-----------------------')
print('Multiple sorting')

print(sorted(student_tuples, key=itemgetter(1,2)))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

print(sorted(student_objects, key=attrgetter('grade', 'age')))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

print('-----------------------')

"""
3rd The Old Way Using Decorate-Sort-Undecorate

This idiom is called Decorate-Sort-Undecorate after its three steps:
-   First, the initial list is decorated with new values that control the sort
order.
-   Second, the decorated list is sorted.
-   Finally, the decorations are removed, creating a list that contains only
the initial values in the new order.

This idiom works because tuples are compared lexicographically; the first items are
compared; if they are the same then the second items are compared, and so on.

The sort is stable – if two items have the same key, their order will be preserved
in the sorted list.
"""

print('3rd The Old Way Using Decorate-Sort-Undecorate')
decorated = [(student.grade, i, student) for i, student in enumerate(student_objects)]
decorated.sort()
print([student for grade, i, student in decorated])              # undecorate
# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
