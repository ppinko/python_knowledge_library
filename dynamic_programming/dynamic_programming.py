"""
Dynamic Programming - is an algorithmic paradigm that solves a given complex
problem by breaking it into subproblems and stores the results of subproblems
to avoid computing the same results again.

Two main properties of problems to be solved using DP:
a) overlapping subproblems
b) optimal substructure

a) overlapping subproblems:

- Dynamic Programming is not useful when there are no common (overlapping)
subproblems because there is no point storing the solutions if they are not
needed again.

- There are two different ways to store the values so that these values can be
reused:
	- Memoization (Top Down)
	- Tabulation (Bottom Up)

a1) Memoization (Top Down) -  it contains a lookup table. Whenever we need the
solution to a subproblem, we first look into the lookup table. If the
precomputed value is there then we return that value, otherwise, we calculate
the value and put the result in the lookup table so that it can be reused later.
"""

# Python program for Memoized version of nth Fibonacci number 
lookup = [None]*(101) 

# Function to calculate nth Fibonacci number 
def fib(n, lookup): 
  
    # Base case 
    if n == 0 or n == 1 : 
        lookup[n] = n 
  
    # If the value is not calculated previously then calculate it 
    if lookup[n] is None: 
        lookup[n] = fib(n-1 , lookup)  + fib(n-2 , lookup)  
  
    # return the value corresponding to that value of n 
    return lookup[n] 

"""
a2) Tabulation (Bottom Up) - The tabulated program for a given problem builds
a table in bottom up fashion and returns the last entry from table. For example,
for the same Fibonacci number, we first calculate fib(0) then fib(1) then fib(2)
then fib(3) and so on. So literally, we are building the solutions of
subproblems bottom-up.
"""

# Python program Tabulated (bottom up) version 
def fib(n): 
  
    # array declaration 
    f = [0]*(n+1) 
  
    # base case assignment 
    f[1] = 1
  
    # calculating the fibonacci and storing the values 
    for i in xrange(2 , n+1): 
        f[i] = f[i-1] + f[i-2] 
    return f[n] 

"""
SUMMARY OVERLAPPING SUBPROBLEMS:

- Both Tabulated and Memoized store the solutions of subproblems.

- In Memoized version, table is filled on demand while in Tabulated version,
starting from the first entry, all entries are filled one by one.

- Unlike the Tabulated version, all entries of the lookup table are not
necessarily filled in Memoized version.

b) optimal substructure:

- A given problems has Optimal Substructure Property if optimal solution of the
given problem can be obtained by using optimal solutions of its subproblems.

- example of appropriate problem: Shortest Path

- example of inappropriate problem: Longest Path
"""


