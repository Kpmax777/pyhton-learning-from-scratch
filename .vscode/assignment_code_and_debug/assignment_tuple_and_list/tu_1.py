""""
Write a Python program to generate a list of powers of 2 less than 100
using list comprehension.
"""

x = [i**2 for i in range(0, 101, 2) if i ** 2]

print(x)
