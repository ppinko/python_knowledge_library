#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:48:31 2019

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

##### EXAMPLE #####

#def test_suite():
#    """ Run the suite of tests for code in this module (this file).
#    """
#    test(absolute_value(17) == 17)
#    test(absolute_value(-17) == 17)
#    test(absolute_value(0) == 0)
#    test(absolute_value(3.14) == 3.14)
#    test(absolute_value(-3.14) == 3.14)
#
#test_suite()        # Here is the call to run the tests
    
def turn_clockwise(x):
    """function returning the next compass point in the clockwise direction"""
    res = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday,
           5:"Friday", 6:"Saturday}
    ans = res.get(x, None)
    return ans