"""
Write a function to remove duplicates from a list and print them.
"""


def input1(lst: list):
    distinct = []
    for i in lst:
        if i not in distinct:
            distinct.append(i)
    print(distinct)


a = [24, 32, 54, 46, 46, 21, 33]
input1(a)
