#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 08:58:10 2019

@author: pawel
"""

filepath = '/home/pawel/Pawel/Python/2019/IT guy/week_2/pi_digits.txt'

#with open(filepath) as file_object:
#    contents = file_object.read()
#    print(contents)
    
#with open(filepath) as file_object:
#    for line in file_object:
#        print(line.rstrip())
#        print('\n')

#with open(filepath) as file_object:
#    lines = file_object.readlines()
#
#for line in lines:
#    print(line.rstrip())
#    
#filename = 'programming.txt'
#with open(filename, 'w') as file_object:
#    file_object.write("I love programming.")

""" Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt. """

#name = input("Please give me your name: ")
#filename = "guest.txt"
#
#with open(filename, 'w') as file_object:
#    file_object.write(name + '\n')

""" Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file. """

filename = "guest.txt"

#with open(filename, 'a') as file_object:
#    while True:
#        answer = input("Please give me your name: ")
#        if answer == 'q':
#            break
#        else:
#            print('Welcome {0}'.format(answer))
#            file_object.write('{0} visited the program\n'.format(answer))

#with open(filename, 'r') as file_object:
#    for line in file_object:
#        print(line.rstrip())
        
#try:
#    print(5/0)
#except ZeroDivisionError:
#    print("You can't divide by zero!")
    
######################################################################
    
#print("Give me two numbers, and I'll divide them.")
#print("Enter 'q' to quit.")
#while True:
#    first_number = input("\nFirst number: ")
#    if first_number == 'q':
#        break
#    second_number = input("Second number: ")
#    try:
#        answer = int(first_number) / int(second_number)
#    except ZeroDivisionError:
#        print("You can't divide by 0!")
#    else:
#        print(answer)

"""One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int , you’ll get a TypeError . Write a program that prompts for
two numbers. Add them together and print the result. Catch the TypeError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number."""

def sum_num (x, y):
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        pass
    else:
        return x+y

#print(sum_num(1,2))
#print(sum_num('1',2))
#print(sum_num('1','ola'))

def get_age():
    age = int(input("Please enter your age: "))
    if age < 0:
        # Create a new instance of an exception
        my_error = ValueError("{0} is not a valid age".format(age))
        raise my_error
    return age

def recursion_depth(number):
    print("Recursion depth number", number)
    try:
        recursion_depth(number + 1)
    except:
        print("I cannot go any deeper into this wormhole.")

def filter(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        if text[0] == "#":
            continue
        # Put any more processing logic here
        outfile.write(text)
    infile.close()
    outfile.close()

#import urllib.request
#
#def retrieve_page(url):
#    """ Retrieve the contents of a web page.
#        The contents is converted to a string before returning it.
#    """
#    my_socket = urllib.request.urlopen(url)
#    dta = str(my_socket.readall())
#    my_socket.close()
#    return dta
#
#the_text = retrieve_page("https://archive.org/stream/2018Fundamentals.ofPython/2018_fundamentals.of-python_djvu.txt")
#print(the_text)
    
"""Write a program that reads a file and writes out a new file with the lines 
in reversed order (i.e. the first line in the old file becomes the last one in 
the new file.)"""

def reverse_file(file_1, file_2):
    text = []
    with open(file_1, 'r') as file_a:
        lines = file_a.readlines()
        for line in lines:
            text.insert(0, line.rstrip())   
    with open(file_2, 'w') as file_b:
        for line in text:
            file_b.write(line)
            file_b.write('\n')

#reverse_file('file_1.txt', 'file_2.txt')
    
"""Write a program that reads a file and prints only those lines that contain 
the substring snake."""

def text_substrings(file, substring):
    """ Gives all the line in text including given substring """
    with open (file, 'r') as file_ed:
        lines = file_ed.readlines()
        for line in lines:
            if substring in line.lower():
                print(line.rstrip())

#text_substrings('snake.txt', 'snake')
                
""" Write a program that reads a text file and produces an output file which 
is a copy of the file, except the first five columns of each line contain a 
four digit line number, followed by a space. Start numbering the first line in 
the output file at 1. Ensure that every line number is formatted to the same 
width in the output file. Use one of your Python programs as test data for 
this exercise: your output should be a printed and numbered listing of the 
Python program. """

def text_format(text, x):
    text_list = text.split()
    trans_text = ''
    char_count = 0
    for i in text_list:
        if char_count + len(i) < x:
            trans_text += str(i) + ' '
            char_count += len(i)+1
        else:
            char_count = 0
            trans_text += '\n' + i + ' '
    return trans_text

#def formatted_file(file):
#    """ Gives back formatted text with indexes of line. """
#    with open(file, 'r') as file_ed:
#        text = file_ed.read()
#    trans_text = text_format(text, 72)
#    with open('formatted_file.txt', 'w') as new_text:
#        for line in lines:
#            new_text.write(line)
#            new_text.write()
#    
#formatted_file('snake.txt')