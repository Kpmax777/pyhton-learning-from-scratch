""""
Q4. Create a function named calSum which takes an 2 integer (n1 and n2)
as an argument. Calculate the sum of all the numbers divisible by 5
between n1 and n2 and return that sum. 
(Make sure that n1 is less than n2)

"""


def calSum(num: int, num2) -> int:
    if num > num2:
        return False
    sum = 0
    start: int = num
    while start <= num2:
        sum = sum + start
        start += 1
    return sum


result = calSum(12, 16) / 5


print(int(result))
