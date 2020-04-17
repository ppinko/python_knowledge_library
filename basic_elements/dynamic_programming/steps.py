"""
Davis has a number of staircases in his house and he likes to climb 
each staircase 1, 2 or 3 steps at a time. Being a very precocious child, 
he wonders how many ways there are to reach the top of the staircase.

n - hight of staircase
"""

def stepPerms(n):
    arr = [1, 2, 3]
    memo = {}
    return rec_steps(n - arr[0], arr[0], memo) + rec_steps(n-arr[1], arr[1], memo) + rec_steps(n-arr[2], arr[2], memo)


def rec_steps(n, k, memo):
    arr = [1, 2, 3]
    if n in memo:
        return memo[n]
    elif n < 0:
        return 0
    elif n == 0:
        to_return = 1
    else:
        to_return = rec_steps(n - arr[0], arr[0], memo) + rec_steps(n-arr[1], arr[1], memo) + rec_steps(n-arr[2], arr[2], memo)
    memo[n] = to_return
    return to_return

n = 3
print(stepPerms(n))
n = 1
print(stepPerms(n))
n = 7
print(stepPerms(n))
n = 30
print(stepPerms(n))
n = 50
print(stepPerms(n))
n = 10
print(stepPerms(n))