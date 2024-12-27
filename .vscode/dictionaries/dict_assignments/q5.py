"""
Write a Python program to check if a dictionary is empty or not.
"""


def func(num: int):

    for values in num.values():
        if None in num:
            print("give rigth inputs")
        else:
            print(values)


my_dict = {"kp": 12, "lalli": None, "mahesh": 94}

func(my_dict)
