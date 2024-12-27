"""
Create a function named calSum() which takes 2 integers n1 and n2 as
a argument. Calculate the sum of all the numbers from n1 and n2 and
RETURN THAT SUM. Also make sure that n1 is smaller than n2. If it is not,
then return “n1 should be smaller”.

"""


def calSum(num: int, num1: int):

    if num <= num1:

        sum = 0

        while num <= num1:
            sum = sum + num  # this increments the the sum varible
            num += 1  # this increments the num varible for
            # while loop iteration

        return sum

    else:
        print("the n1 is smaller than n2")


num: int = int(input("enter the first number:"))
num1: int = int(input("enter second number:"))

result = calSum(num, num1)
print(result)
