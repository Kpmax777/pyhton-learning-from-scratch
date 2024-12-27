"""
Write a Python program to generate and print a dictionary that
contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

"""


def func(num: dict):
    output = {}
    for values in range(1, num + 1):
        output[values] = values**2

    return output


my_dict = int(input("enter the number : "))

print(func(my_dict))
