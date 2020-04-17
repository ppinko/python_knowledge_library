# -*- coding: utf-8 -*-
"""
Pawel
2019/10/31
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

def r_sum(nested_num_list):
    tot = 0
    for element in nested_num_list:
        if type(element) == type([]):
            tot += r_sum(element)
        else:
            tot += element
    return tot

##TEST
#print(r_sum([1, 2, 3]))
#print(r_sum([1]))
#print(r_sum([1, 2, [1, 2]]))

def r_max(nxs):
    """
      Find the maximum in a recursive structure of lists
      within other lists.
      Precondition: No lists or sublists are empty.
    """
    largest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e

        if first_time or val > largest:
            largest = val
            first_time = False

    return largest

#test(r_max([2, 9, [1, 13], 8, 6]) == 13)
#test(r_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100)
#test(r_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100)
#test(r_max(["joe", ["sam", "ben"]]) == "sam")

#def fib(n):
#    if n <= 1:
#        return n
#    t = fib(n-1) + fib(n-2)
#    return t

#import time
#t0 = time.clock()
#n = 35
#result = fib(n)
#t1 = time.clock()
#
#print("fib({0}) = {1}, ({2:.2f} secs)".format(n, result, t1-t0))

#############################################################################
#############################################################################
#############################################################################

"""
TASK 1
Write a function, recursive_min, that returns the smallest value in a nested 
number list. Assume there are no empty lists or sublists.
"""

def recursive_min(x):
    lowest = None
    for element in x:
        if type(element) == type([]):
            val = recursive_min(element)
        else:
            val = element        
        if lowest == None:
            lowest = val
        elif val < lowest:
            lowest = val
    return lowest
            
    
#test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
#test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
#test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
#test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)

"""
TASK 2
Write a function count that returns the number of occurrences of target in 
a nested list
"""

def count (number, list):
    found = 0
    for i in list:
        if type(i) == type([]):
            found += count(number, i)
        elif i == number:
            found += 1
    return found        

#test(count(2, []) == 0)
#test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
#test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
#test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
#test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
#test(count("a",
#     [["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]) == 4)

"""
TASK 3
Write a function flatten that returns a simple list containing all the values 
in a nested list. 
"""

def flatten(x):
    ans = []
    for i in x:
        if type(i) == type([]):
            ans.extend(flatten(i))
        else:
            ans.append(i)
    return ans
            
#test(flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
#test(flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
#test(flatten([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6])
#test(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) ==
#              ["this","a","thing","a","is","a","easy"])
#test(flatten([]) == [])

"""
TASK 4
Rewrite the fibonacci algorithm without using recursion. Can you find bigger 
terms of the sequence? Can you find fib(200)?
"""

def fib(n):
    d = {0:1, 1:1}
    if n == 0 or n ==1:
        return 1
    i = 2
    while i <= n:
        d[i] = d[i-2] + d[i-1]
        i += 1
    return d[n]
        
#print(fib(200))
    
import os

def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix = ""):
    """ Print recursive listing of contents of path """
    if prefix == "":  # Detect outermost call, print a heading
        print("Folder listing for", path)
        prefix = "| "

    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix+f)                    # Print the line
        fullname = os.path.join(path, f)   # Turn name into full pathname
        if os.path.isdir(fullname):        # If a directory, recurse.
            print_files(fullname, prefix + "| ")

#print(print_files('/home/lx/all/linux'))
            
"""
TASK 5
Write a program that walks a directory structure (as in the last section of 
this chapter), but instead of printing filenames, it returns a list of all the 
full paths of files in the directory or the subdirectories. (Don’t include 
directories in this list — just files.)
"""

def print_files_path(path):
    """ Print recursive all file paths excluding directories """
    dirlist = os.listdir(path)
    for f in dirlist:
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            print_files_path(fullname)
        else:
            print(fullname)

#print_files_path('/home/lx/all/linux')

"""
TASK 6
Write a program named litter.py that creates an empty file named trash.txt in 
each subdirectory of a directory tree given the root of the tree as an argument 
(or the current directory as a default). Now write a program named cleanup.py 
that removes all these files.
"""

def litter(path):
    dirlist = os.listdir(path)
    f2 = '/trash.txt'
    for f in dirlist:
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            file = open(fullname + f2, 'w')
            file.close()
            litter(fullname)

#litter('/home/lx/all/linux')
            
def cleanup(path):
    dirlist = os.listdir(path)
    f2 = '/trash.txt'
    for f in dirlist:
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            os.remove(fullname + f2)
            cleanup(fullname)

#cleanup('/home/lx/all/linux')