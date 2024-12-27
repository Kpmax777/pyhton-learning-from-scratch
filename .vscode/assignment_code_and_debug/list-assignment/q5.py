"""
Write a program to put all the common elements (in 2 lists) in another
list and print it using function.
"""


def func(num: list, num1: list):
    result = []
    for i in num:
        for j in num1:
            if i == j:
                result.append(i)

    print(result)


a = [21, 42, 34, 55, 66]
b = [32, 12, 42, 55, 61]

func(a, b)
