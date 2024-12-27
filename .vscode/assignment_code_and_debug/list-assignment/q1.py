"""
. Make a list of your own. Make two more empty list like odd and even.
Put all the even numbers from original list to even and odd numbers to
odd and print both lists. (Don’t remove anything from original one).
"""


def input1(num: list):
    even = []
    odd = []

    for i in num:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print(even)
    print(odd)


a = [24, 32, 54, 46, 21, 33]
input1(a)
print(input1)
