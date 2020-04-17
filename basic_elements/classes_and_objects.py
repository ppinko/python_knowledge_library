#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:56:47 2019

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

class Point():
    """ Basic operations with points."""
    
    def __init__(self, x = 0, y = 0):
        """Initilize attributes of the point."""
        self.x = x
        self.y = y
    
    def __str__(self):
        """Creates a string."""
        return "({0}, {1})".format(self.x, self.y)
    
    def change_cordinates(self, x1, y1):
        """Changes coordinates of the point."""
        self.x = x1
        self.y = y1
    
    def distance_to_origin(self):
        """Calculates distance to origin."""
        distance = (self.x ** 2 + self.y **2) ** 0.5
        return distance
    
    def distance_to_point(self, p1):
        """Calculates distance to point."""
        distance = ((self.x - p1.x) **2 + (self.y - p1.y) **2) ** 0.5
        return distance
    
    def reflect_x(self):
        """Creates reflection of point to x axis."""
        p2 = Point(-self.x, self.y)
        return p2
    
    def slope_to_origin(self):
        """Calculates slope to origin."""
        if self.x == 0:
            return "Point lays on y axis"
        elif self.y == 0:
            return "Point lays on x axis"        
        else:
            slope = self.y/self.x
            return slope
    
    def get_line_to(self, p2):
        """Calculates a and b coefficients from y = ax + b"""
        """ y1- ax1 = y2 - ax2
        a = (y1-y2)/(x1-x2)
        b = y1 - a * x1"""
        if self.x == p2.x:
            return 'x = {0}'.format(self.x)
        elif self.y == p2.y:
            return 'y = {0}'.format(self.y)
        else:
            a = (self.y - p2.y)/(self.x - p2.x)
            b = self.y - a * self.x
            return (a, b)

    def get_cordinates(self):
        """Tuple representing point."""
        return (self.x, self.y)

def same_coordinates(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

class SMS_store():
    """Basic representation of sms system."""
    
    def __init__(self, list_of_sms = [], number_of_sms = 0):
        """Initiliaze attributes."""
        self.list_of_sms = list_of_sms
        self.number_of_sms = number_of_sms
    
    def add_new_arrival(self, from_number, time_arrived, text_of_SMS, 
                        has_been_viewed = False):
        """New message."""
        self.list_of_sms.append([from_number, time_arrived, text_of_SMS, 
                                 has_been_viewed])
        
    def message_count(self):
        """Number of messages in inbox."""
        return len(self.list_of_sms)
    
    def get_unread_indexes(self):
        """Indexes of unread messages."""
        unread_sms = []
        k = 0
        for i in self.list_of_sms:
            if i[3] == False:
                unread_sms.append(k)
                k += 1
            else:
                k += 1
        return unread_sms
    
    def get_message(self, i):
        """Shows a given message."""
        self.list_of_sms[i][3] = True
        return print((tuple(self.list_of_sms[i])))
    
    def delete(self, i):
        """Delete message."""
        del self.list_of_sms[i]
    
    def clear_all(self):
        """Clears all messages."""
        self.list_of_sms = []

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy
        
    def area(self):
        """ Give ares of rectangle """
        return self.width * self.height
    
    def perimeter(self):
        """ Give perimeter of rectangle """
        return 2 * (self.width + self.height)
    
    def flip(self):
        """ Swap width and height of rectangle """
        (t1, t2) = (self.width, self.height)
        self.width = t2
        self.height = t1
        
    def contains(self, point):
        """ Check if point lays in rectangle """
        if self.corner.x <= point.x < (self.corner.x + self.width) and self.corner.y <= point.y < (self.corner.y + self.height):
            return True
        else:
            return False

    def all_corners(self):
        """ Coordinates of all corners """
        p1 = Point(self.corner.x, self.corner.y)
        p2 = Point(self.corner.x + self.width, self.corner.y)
        p3 = Point(self.corner.x, self.corner.y + self.height)
        p4 = Point(self.corner.x + self.width, self.corner.y + self.height)
        return (p1, p2, p3, p4)
    
    def overlap(self, r1):
        """ Check overlap between two rectangulars """
        rc = self.all_corners()
        rc1 = r1.all_corners()
        for i in rc:
            if r1.contains(i):
                return True
        for j in rc1:
            if self.contains(j):
                return True
        return False
    
#r = Rectangle(Point(0, 0), 10, 5)
#test(r.area() == 50)
#r = Rectangle(Point(0, 0), 10, 5)
#test(r.perimeter() == 30)
#r = Rectangle(Point(100, 50), 10, 5)
#test(r.width == 10 and r.height == 5)
#r.flip()
#test(r.width == 5 and r.height == 10)
#r = Rectangle(Point(0, 0), 10, 5)
#test(r.contains(Point(0, 0)))
#test(r.contains(Point(3, 3)))
#test(not r.contains(Point(3, 7)))
#test(not r.contains(Point(3, 5)))
#test(r.contains(Point(3, 4.99999)))
#test(not r.contains(Point(-3, -3)))
#r1 = Rectangle(Point(0, 0), 10, 5)
#r2 = Rectangle(Point(-5, -5), 1, 1)
#test(not r1.overlap(r2))
#r1 = Rectangle(Point(0, 0), 10, 5)
#r2 = Rectangle(Point(-2, -5), 8, 7)
#test(r1.overlap(r2))