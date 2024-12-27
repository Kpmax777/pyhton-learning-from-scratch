"""
1. Without Paramters, without Return
2. With Paramters, without Return
3. Without Paramters, with Return
4. With Paramters, with Return
"""


def add():
    num: int = int(input("enter number: "))
    num1: int = int(input("enter the seceond number: "))

    print(num1 + num)


def sub():
    num: int = int(input("enter number: "))
    num1: int = int(input("enter number: "))
    subtraction = num - num1
    print(subtraction)


def div():
    num1: int = int(input("enter the number: "))
    num: int = int(input("enter the second number: "))
    print(num1 / num)


add()
sub()
div()
