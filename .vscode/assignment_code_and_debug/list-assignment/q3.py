"""
Write a Python function that takes two lists and returns True if they
have at least one common element.
"""


def func(num: list, num1: list) -> int:
    for i in num:
        for j in num1:

            if i == j:
                print("true", i)


list1 = [12, 41, 55, 67, 90, 13]
list2 = [41, 67, 21, 44, 45, 66]

func(list1, list2)
