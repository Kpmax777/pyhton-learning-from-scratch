"""
Write a Python Program to find sum and average of List in Python.

"""


def func(num: list):
    sum = 0
    avg = 0
    for i in num:
        sum = sum + i

    avg = sum / len(num)

    print(avg)
    print(sum)


a = [24, 24, 24]

func(a)
