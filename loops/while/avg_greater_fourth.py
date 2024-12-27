"""
Write a Python program that takes four numbers from the user.
Implement a function to find the average of the first three numbers. Then,
create another function to check if the average is greater than or equal to
the fourth number. Make sure to use these two functions to determine and

"""


def avg(num1: int, num2: int, num3: int) -> float:
    average = (num1 + num2 + num3) / 3
    return average


def avg_g(m, num4):

    return m < num4


avg_result = avg(66, 72, 67)
print(round(avg_result, 2))
# result = avg_g(avg_result, 69)


if avg_g(avg_result, 69):
    print("fouth number is greater than avg")
else:
    print("fourth number is lesser than avg")
