#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 18:50:45 2019

@author: lx
"""

##############################################################################
### LESSON

import sys
from recursion import test

def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for (i, v) in enumerate(xs):
       if v == target:
           return i
    return -1

#friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
#test(search_linear(friends, "Zoe") == 1)
#test(search_linear(friends, "Joe") == 0)
#test(search_linear(friends, "Paris") == 6)
#test(search_linear(friends, "Bill") == -1)
    
def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    for w in wds:
        if (search_linear(vocab, w) < 0):
            result.append(w)
    return result

#vocab = ["apple", "boy", "dog", "down",
#                          "fell", "girl", "grass", "the", "tree"]
#book_words = "the apple fell from the tree to the grass".split()
#test(find_unknown_words(vocab, book_words) == ["from", "to"])
#test(find_unknown_words([], book_words) == book_words)
#test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])

def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds

#bigger_vocab = load_words_from_file("vocab.txt")
#print("There are {0} words in the vocab, starting with\n {1} "
#              .format(len(bigger_vocab), bigger_vocab[:6]))

def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
        and all in lowercase.
    """

    my_substitutions = the_text.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds

def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds

#book_words = get_words_in_book("AliceInWonderland.txt")
#print("There are {0} words in the book, the first 100 are\n{1}".
#           format(len(book_words), book_words[:100]))
    
import time

#t0 = time.clock()
#missing_words = find_unknown_words(bigger_vocab, book_words)
#t1 = time.clock()
#print("There are {0} unknown words.".format(len(missing_words)))
#print("That took {0:.4f} seconds.".format(t1-t0))

##### BINARY SEARCH #####

def search_binary(xs, target):
    """ Find and return the index of key in sequence xs """
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:   # If region of interest (ROI) becomes empty
           return -1

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = xs[mid_index]

        # print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'"
        #       .format(lb, ub, ub-lb, item_at_mid, target))

        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index      # Found it!
        if item_at_mid < target:
            lb = mid_index + 1    # Use upper half of ROI next time
        else:
            ub = mid_index        # Use lower half of ROI next time

#xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]
#test(search_binary(xs, 20) == -1)
#test(search_binary(xs, 99) == -1)
#test(search_binary(xs, 1) == -1)
#for (i, v) in enumerate(xs):
#    test(search_binary(xs, v) == i)
            
def remove_adjacent_dups(xs):
    """ Return a new list in which all adjacent
        duplicates from xs have been removed.
    """
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e

    return result

#test(remove_adjacent_dups([1,2,3,3,3,3,5,6,9,9]) == [1,2,3,5,6,9])
#test(remove_adjacent_dups([]) == [])
#test(remove_adjacent_dups(["a", "big", "big", "bite", "dog"]) ==
#                                   ["a", "big", "bite", "dog"])
    
def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            result.extend(ys[yi:]) # Add remaining items from ys
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1

#xs = [1,3,5,7,9,11,13,15,17,19]
#ys = [4,8,12,16,20,24]
#zs = xs+ys
#zs.sort()
#test(merge(xs, []) == xs)
#test(merge([], ys) == ys)
#test(merge([], []) == [])
#test(merge(xs, ys) == zs)
#test(merge([1,2,3], [3,4,5]) == [1,2,3,3,4,5])
#test(merge(["a", "big", "cat"], ["big", "bite", "dog"]) ==
#               ["a", "big", "big", "bite", "cat", "dog"])

##############################################################################
"""
TASK 1
Every week a computer scientist buys four lotto tickets. She always chooses the 
same prime numbers, with the hope that if she ever hits the jackpot, she will 
be able to go onto TV and Facebook and tell everyone her secret. This will 
suddenly create widespread public interest in prime numbers, and will be the 
trigger event that ushers in a new age of enlightenment. She represents her 
weekly tickets in Python as a list of lists.
a) Each lotto draw takes six random balls, numbered from 1 to 49. Write a 
function to return a lotto draw.
b) Write a function that compares a single ticket and a draw, and returns the 
number of correct picks on that ticket.
c) Write a function that takes a list of tickets and a draw, and returns a list 
telling how many picks were correct on each ticket.
d) Write a function that takes a list of integers, and returns the number of 
primes in the list.
e) Write a function to discover whether the computer scientist has missed any 
prime numbers in her selection of the four tickets. Return a list of all primes 
that she has missed
f) Write a function that repeatedly makes a new draw, and compares the draw to 
the four tickets
Count how many draws are needed until one of the computer 
scientist’s tickets has at least 3 correct picks. Try the experiment twenty 
times, and average out the number of draws needed.


"""

import random

def lotto():
    """ Generate lotto results """
    x = random.sample(range(1, 50), 6)
    return x

## test lotto
#x = lotto()
#test(type(x) == type([]))
#test(len(x) == 6)

def lotto_match(draw, picks):
    """ Check number of correct picks """
    match = 0
    for ball in draw:
        if ball in picks:
            match += 1
    return match

#test(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]) == 3)

def lotto_matches(draw, tickets):
    """ Check matches in several coupons """
    matches = []
    for ticket in tickets:
        x = lotto_match(draw, ticket)
        matches.append(x)
    return matches

#test(lotto_matches([42,4,7,11,1,13], my_tickets) == [1,2,3,1])

def is_prime(x):
    """ Prove if number is prime """
    if x == 0 or x == 1:
        return 0
    for i in range(2, x//2 +1):
        if x % i == 0:
            return 0
    return 1
        
#test(is_prime(0) == 0)
#test(is_prime(1) == 0)
#test(is_prime(2) == 1)
#test(is_prime(4) == 0)
#test(is_prime(7) == 1)

def primes_in(draw):
    """ Check number of prime numbers in a coupon """
    prime = 0
    for number in draw:
        if is_prime(number) == 1:
            prime += 1
    return prime

#test(primes_in([42, 4, 7, 11, 1, 13]) == 3)

def primes_to(limit):
    """ Generate prime numbers to given limit (including) """
    primes = []
    for i in range(2, limit+1):
        if is_prime(i) == 1:
            primes.append(i)
    return primes
    
def prime_misses(tickets):
    """ Check missied primes in lotto """
    primes = primes_to(49)
    choices = []
    for ticket in tickets:
        for number in ticket:
            if number not in choices:
                choices.append(number)
    for choice in choices:
        primes.remove(choice)
    return primes
    
my_tickets = [ [ 7, 17, 37, 19, 23, 43],
               [ 7,  2, 13, 41, 31, 43],
               [ 2,  5,  7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]

#test(prime_misses(my_tickets) == [3, 29, 47])

#def lotto_1000000 (coupons, guesses):
#    """ Generates good coupons in 1 000 000 of tries """
#    count = 0
#    for i in range(1000000):
#        results = lotto()
#        x = lotto_matches(results, coupons)
#        for i in x:
#            if i >= guesses:
#                count += 1
#                break
#    return count

def lotto_1000000 (coupons, guesses):
    i = 1
    while True:
        results = lotto()
        x = lotto_matches(results, coupons)
        for j in x:
            if j >= guesses:
                return i
        i += 1

#print(lotto_1000000(my_tickets, 3))