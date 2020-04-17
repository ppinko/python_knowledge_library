#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 13:26:45 2019

@author: pawel
"""

'''You go on a wonderful holiday (perhaps to jail, if you don’t like happy 
exercises) leaving on day number 3 (a Wednesday). You return home after 137 
sleeps. Write a general version of the program which asks for the starting day 
number, and the length of your stay, and it will tell you the name of day of 
the week you will return on.'''

def day_week(start,end):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 
            'Saturday', 'Sunday']
    x = (start + end) % 7
    return days[x-1]

#print(day_week(1,1))
#print(day_week(4,11))
    
'''Write a function find_hypot which, given the length of two sides of a right-
angled triangle, returns the length of the hypotenuse. (Hint: x ** 0.5 will 
return the square root.)'''

def find_hypot(a, b):
    if a <= 0 or b <= 0:
        return print('length must be a positive number')
    ans = (a ** 2 + b ** 2) ** 0.5
    return ans

#print(find_hypot(3,4))
#print(find_hypot(3,5))

'''Write a function is_rightangled which, given the length of three sides of a 
triangle, will determine whether the triangle is right-angled. Assume that the 
third argument to the function is always the longest side. It will return True 
if the triangle is right-angled, or False otherwise.'''

def is_rightangled(c, d, f):
    k = [c,d,f]
    k.sort()
    comp = find_hypot(k[0],k[1])
    return abs(comp - k[2]) < 0.000001

#print(is_rightangled(5,3,4))
#print(is_rightangled(3,4,5))
#print(is_rightangled(5,4,6))