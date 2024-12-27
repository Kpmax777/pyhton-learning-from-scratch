"""
Make two lists of same length and pass it to a function. Return a third
list where each element is the sum of index.
"""


def func(num1: list, num2: list):
    sum = []
    for i in range(0, len(num1)):

        result = num1[i] + num2[i]
        sum.append(result)
    print(sum)


a = [21, 33, 21]
b = [22, 41, 54]

func(a, b)
