"""
Write a function named armstrongRange which accepts 2 integers n1
and n2. Print all the numbers from n1 to n2 which are armstrong numbers.
"""

# 100


def func(n, n1):
    for i in range(n, n1):
        num = i
        sum = 0
        while num > 0:
            re = num % 10
            sum = sum + (re**3)
            num = num // 10
        if num == sum:
            print(num, "is armstrong number")


n = 1
n1 = 1000
func(n, n1)
