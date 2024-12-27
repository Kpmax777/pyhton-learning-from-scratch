"""
. Create a function named printPattern that takes one integer (num) as
an argument. Print from -num to num. Also keep in mind number passed as
an argument can be negative or positive.
"""


def num(number: int) -> int:
    if number < 0:
        b = -(number)

        while b >= number:
            print(b)
            b = b - 1
    else:
        b = -number

        while b <= number:
            print(b)
            b = b + 1


name = int(input("enter a number:"))
num(name)
