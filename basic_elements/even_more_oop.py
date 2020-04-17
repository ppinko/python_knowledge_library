#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:57:35 2019

@author: lx
"""

import sys
from recursion import test

class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a MyTime object initialized to hrs, mins, secs """
        # Calculate total seconds to represent
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs // 3600        # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        return '{0} hours, {1} minutes, {2} seconds'.format(self.hours, 
               self.minutes, self.seconds)

    def increment(self, seconds):
        totalsecs = self.to_seconds() + seconds
        self.hours = totalsecs // 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def to_seconds(self):
        """ Return the number of seconds represented
            by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds
    
    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > time2.to_seconds()
    
    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())
    
    def __sub__(self, other):
        return MyTime(0, 0, self.to_seconds() - other.to_seconds())
    
    """ TASK """
    """Turn the function 'between' into a method in the MyTime class."""
    def between(self, t1, t2):
        """ Check if given time is between two other specified """
        s0 = self.to_seconds()
        s1 = t1.to_seconds()
        s2 = t2.to_seconds()
        return s1 <= s0 < s2
    
    """ Overload the '>' operator(s) """
    
    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()
    
    
t1 = MyTime(1, 15, 42)
t2 = MyTime(3, 50, 30)
t3 = MyTime(2, 50, 30)
t4 = MyTime(0, 50, 30)
t5 = MyTime(5, 50, 30)
t6 = MyTime(1, 15, 42)
t7 = MyTime(3, 50, 30)
#test(t3.between(t1, t2) == True)
#test(t4.between(t1, t2) == False)
#test(t5.between(t1, t2) == False)
#test(t6.between(t1, t2) == True)
#test(t7.between(t1, t2) == False)    
#test(t1 > t2 == False)
#test(t2 > t3 == True)
#test(t1 > t6 == False)
#test(t1.increment(10) == '1 hours, 15 minutes, 52 seconds')
#print(t1)
#test(t1.increment(60) == '1 hours, 16 minutes, 52 seconds')
#print(t1)
#test(t1.increment(-70) == '1 hours, 15 minutes, 42 seconds')
#print(t1)

#time1 = MyTime(10, 20, 30)
#test(str(time1) == '10 hours, 20 minutes, 30 seconds')
#print(time1)

#def add_time(t1, t2):
#    secs = t1.to_seconds() + t2.to_seconds()
#    return MyTime(0, 0, secs)

#current_time = MyTime(9, 14, 30)
#bread_time = MyTime(3, 35, 0)
#done_time = add_time(current_time, bread_time)
#print(done_time)
    
###############################################################################
""" TASK """
"""Write a Boolean function between that takes two MyTime objects, t1 and t2, 
as arguments, and returns True if the invoking object falls between the two 
times. Assume t1 <= t2, and make the test closed at the lower bound and open 
at the upper bound, i.e. return True if t1 <= obj < t2."""

def between(t1, t2, t3):
    s1 = t1.to_seconds()
    s2 = t2.to_seconds()
    s3 = t3.to_seconds()
    return s1 <= s3 < s2
    
#t1 = MyTime(1, 15, 42)
#t2 = MyTime(3, 50, 30)
#t3 = MyTime(2, 50, 30)
#t4 = MyTime(0, 50, 30)
#t5 = MyTime(5, 50, 30)
#t6 = MyTime(1, 15, 42)
#t7 = MyTime(3, 50, 30)
#test(between(t1, t2, t3) == True)
#test(between(t1, t2, t4) == False)
#test(between(t1, t2, t5) == False)
#test(between(t1, t2, t6) == True)
#test(between(t1, t2, t7) == False)