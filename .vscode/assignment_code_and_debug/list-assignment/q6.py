"""
Write a program to remove the nth index element from a list using a
function.
"""


def func(num: list, n: int):
    num.pop(n)
    print(num)


a = [3, 56, 34, 21, 56, 45]
c = len(a) - 1
func(a, c)
