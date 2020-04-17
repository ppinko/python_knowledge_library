#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:05:20 2019

@author: pawel
"""

'''6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name , last_name , age , and city . Print each
piece of information stored in your dictionary.'''

paulina = {'first_name': 'paulina', 'last_name': 'czynsz', 'age': 30, 
           'city': 'herborn',
           }

'''Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.'''

#rivers = {}
#rivers['wisla']='poland'
#rivers['amazonia']='brazil'
#rivers['ren']='germany'
#
#for k,v in rivers.items():
#    x = '{0} runs through {1}'.format(k,v)
#    print(x)
#print('\n')
#
#for k in rivers.keys():
#    print(k)
#print('\n')
#
#for k in set(rivers.values()):
#    print(k)
#print('\n')

'''Write a program that reads a string and returns a table of the letters of 
the alphabet in alphabetical order which occur in the string together with the 
number of times each letter occurs. Case should be ignored.'''

text = 'ThiS is String with Upper and lower case Letters'

def count_letter(text):
    dic = {}
    text_for = text.lower().replace(' ','')
    for letter in text_for:
        dic[letter] = dic.get(letter, 0) + 1
    sor_keys = list(dic.keys())
    sor_keys.sort()
    for key in sor_keys:
        print(key, ' ', dic[key])

#count_letter(text)