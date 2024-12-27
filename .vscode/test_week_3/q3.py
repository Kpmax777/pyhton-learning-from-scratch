"""
Write a Python program to check if a triangle is equilateral, isosceles or
scalene.
"""


def triangle(s: list):

    if s[0] == s[1] == s[2]:
        print("eq triangle")
    elif s[0] == s[1] or s[1] == s[2] or s[2] == s[0]:
        print("iso triangle")
    else:
        print("scalene triangle")


l = []

for i in range(0, 3):
    var = int(input("enter a number :"))

    l.append(var)

if l[0] + l[1] > l[2] and l[0] + l[2] > l[1] and l[2] + l[1] > l[0]:

    triangle(l)
else:
    print("give proper values")
