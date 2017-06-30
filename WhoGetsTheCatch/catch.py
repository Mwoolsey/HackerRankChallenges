#!/bin/python

import sys

# n = number of catchers
# x = position of venotoise
# X = position of catchers
# V = speed of catchers
def whoGetsTheCatch(n, x, X, V):
    # Complete this function
    winner = -1
    low_time = float('Inf')
    for index, position in enumerate(X):
        time = abs(position - x)/V[index]
        if time < low_time:
            low_time = time
            winner = index
        elif time == low_time:
            winner = -1
    return winner

#  Return the index of the catcher who gets the catch, or -1 if no one gets the catch.
n, x = raw_input().strip().split(' ')
n, x = [int(n), int(x)]
X = map(int, raw_input().strip().split(' '))
V = map(int, raw_input().strip().split(' '))
result = whoGetsTheCatch(n, x, X, V)
print(result)
