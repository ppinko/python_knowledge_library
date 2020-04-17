#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:48:33 2019

@author: pawel
"""

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

"""The four compass points can be abbreviated by single-letter strings as “N”, 
“E”, “S”, and “W”. Write a function turn_clockwise that takes one of these four 
compass points as its parameter, and returns the next compass point in the 
clockwise direction. You might ask “What if the argument to the function is 
some other value?” For all other cases, the function should return the value 
None """

def turn_clockwise(x):
    """function returning the next compass point in the clockwise direction"""
    res = {"N":"E", "E":"S", "S":"W", "W":"N"}
    ans = res.get(x, None)
    return ans

#test(turn_clockwise("N") == "E")
#test(turn_clockwise("W") == "N")
#test(turn_clockwise(42) == None)
#test(turn_clockwise("rubbish") == None)
    
"""Write a function day_name that converts an integer number 0 to 6 into the 
name of a day. Assume day 0 is “Sunday”. Once again, return None if the 
arguments to the function are not valid. """
    
def day_name(x):
    """function returning the next compass point in the clockwise direction"""
    res = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 
           5:"Friday", 6:"Saturday"}
    ans = res.get(x, None)
    return ans

#test(day_name(3) == "Wednesday")
#test(day_name(6) == "Saturday")
#test(day_name(42) == None)

"""Write the inverse function day_num which is given a day name, and returns 
its number """

def day_num(x):
    """function returning the next compass point in the clockwise direction"""
    res = {"Sunday":0, "Monday":1, "Tuesday":2, "Wednesday":3, "Thursday":4, 
           "Friday":5, "Saturday":6}
    ans = res.get(x, None)
    return ans

#test(day_num("Friday") == 5)
#test(day_num("Sunday") == 0)
#test(day_num(day_name(3)) == 3)
#test(day_name(day_num("Thursday")) == "Thursday")
    
"""Write a function that helps answer questions like ‘“Today is Wednesday. I 
leave on holiday in 19 days time. What day will that be?”’ So the function must 
take a day name and a delta argument — the number of days to add — and should 
return the resulting day name"""

def day_add(day, delta):
    x = day_num(day)
    x += delta
    y = day_name(x%7)
    return y

#test(day_add("Monday", 4) ==  "Friday")
#test(day_add("Tuesday", 0) == "Tuesday")
#test(day_add("Tuesday", 14) == "Tuesday")
#test(day_add("Sunday", 100) == "Tuesday")
#test(day_add("Sunday", -1) == "Saturday")
#test(day_add("Sunday", -7) == "Sunday")
#test(day_add("Tuesday", -100) == "Sunday")
    
"""Write a function days_in_month which takes the name of a month, and returns 
the number of days in the month. Ignore leap years"""

def days_in_month(x):
    """function returning days in the month"""
    res = {"January":31, "February":28, "March":31, "April":30, "May":31, 
           "June":30, "July":31, "August":31, "September":30, "October":31,
           "November":30, "December":31}
    ans = res.get(x, None)
    return ans

#test(days_in_month("February") == 28)
#test(days_in_month("December") == 31)
    
"""Write a function to_secs that converts hours, minutes and seconds to a total 
number of seconds."""
"""Extend to_secs so that it can cope with real values as inputs. It should 
always return an integer number of seconds (truncated towards zero)"""

def to_secs(h, m, s):
    ans = 3600*h + 60*m +s
    return int(ans)

#test(to_secs(2, 30, 10) == 9010)
#test(to_secs(2, 0, 0) == 7200)
#test(to_secs(0, 2, 0) == 120)
#test(to_secs(0, 0, 42) == 42)
#test(to_secs(0, -10, 10) == -590)
#test(to_secs(2.5, 0, 10.71) == 9010)
#test(to_secs(2.433,0,0) == 8758)
    
"""Write a compare function that returns 1 if a > b, 0 if a == b, and -1 if 
a < b"""

def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    elif a < b:
        return -1

#test(compare(5, 4) == 1)
#test(compare(7, 7) == 0)
#test(compare(2, 3) == -1)
#test(compare(42, 1) == 1)
        
"""Write a function slope(x1, y1, x2, y2) that returns the slope of the line 
through the points (x1, y1) and (x2, y2). Then use a call to slope in a new 
function named intercept(x1, y1, x2, y2) that returns the y-intercept of the 
line through the points (x1, y1) and (x2, y2)"""

def slope(x1, y1, x2, y2):
    """y=ax+b -> b=y1-ax1
    y=ax+b -> a=(y2-b)x2
    a=(y2-y1+ax1)x2 -> ax2=ax1+y2-y1 -> a(x2-x1)=y2-y1
    a=(y2-y1)/(x2-x1)"""
    return (y2-y1)/(x2-x1)

#test(slope(5, 3, 4, 2) == 1.0)
#test(slope(1, 2, 3, 2) == 0.0)
#test(slope(1, 2, 3, 3) == 0.5)
#test(slope(2, 4, 1, 2) == 2.0)

def intercept(x1, y1, x2, y2):
    a = slope(x1, y1, x2, y2)
    b = y1-a*x1
    return b
    
#test(intercept(1, 6, 3, 12) == 3.0)
#test(intercept(6, 1, 1, 6) == 7.0)
#test(intercept(4, 6, 12, 8) == 5.0)