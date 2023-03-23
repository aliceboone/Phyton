"""
Python Data Structures - A Game-Based Approach
Stack challenge
Robin Andrews - https://compucademy.net/
"""

import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

# Your solution here.
# Create a Stack
for char in string:
    s.push(char)

print(s)
while not s.is_empty():
    reversed_string = reversed_string + s.pop()

print(reversed_string)
