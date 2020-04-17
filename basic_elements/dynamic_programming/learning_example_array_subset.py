"""
Find a number of subsets of arr, which sum is equal to 16.

arr = [2, 4, 6, 10]
"""

arr = [2, 4, 6, 10]
total = 16

### FIRST SOLUTION - NAIVE RECURSION

def count_sets(arr, total):
    ''' Main function counting the subsets '''
    return rec(arr, total, len(arr) - 1)

def rec(arr, total, i):
    ''' Recursive function '''
    
    # Base cases
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    
    # conditions
    elif total < arr[i]:
        return rec(arr, total, i-1)
    else:
        return rec(arr, total - arr[i], i - 1) + rec(arr, total, i - 1)

print(count_sets(arr, total))

### SECOND SOLUTION - MEMOIZED APPROACH (DYNAMIC PROGRAMMING)

def count_sets_dp(arr, total):
    ''' Main function counting the subsets '''
    mem = {}
    return dp(arr, total, len(arr) - 1, mem)

def dp(arr, total, i, mem):
    ''' Recursive function '''
    
    # Checking whether if the value is already in dict
    key = str(total) + ':' + str(i) # generating a unique key
    if key in mem:
        return mem[key]

    # Base cases
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    
    # conditions
    elif total < arr[i]:
        to_return = dp(arr, total, i-1, mem)
    else:
        to_return = (dp(arr, total - arr[i], i - 1, mem)) + (dp(arr, total, i - 1, mem))
    mem[key] = to_return
    return to_return

print(count_sets_dp(arr, total))