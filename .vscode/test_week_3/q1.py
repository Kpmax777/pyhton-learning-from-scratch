"""
Write a function named notPrimeNumbers which accepts 2 integers n1
and n2. Print all the numbers from n1 to n2 which are not prime.

"""


def notPrimeNumbers(num1: int, num2: int) -> int:
    sum = 0
    for i in range(num1, num2):
        count = 0
        for j in range(1, i + 1):

            if i % j == 0:
                count = count + 1
        if count != 2:
            print(i)


n1 = int(input("enter a number: "))
n2 = int(input("enter a second number:"))

notPrimeNumbers(n1, n2)
