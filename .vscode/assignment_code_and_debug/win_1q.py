"""
Q1. Create a function named div_by_3_and_5 which takes 2 integers as a
arguments (n1,n2), and print all the numbers divisible by 3 and 5 between
n1 and n2.

"""


def div_by_3_and_5(num: int, num1: int) -> int:
    start: int = num
    end: int = num1

    while start <= end:

        if start % 3 == 0 and start % 5 == 0:
            print(start)
        start = start + 1


div_by_3_and_5(15, 100)
