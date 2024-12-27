""""
Create a function named multiplicationTable that takes an integer
num as an argument. Print the multiplication table of that number
 up to 10
numbers.
"""


def multiplicationTable(num: int):
    mutliple: int = 0
    start = 1
    while start <= 10:
        mutliple = num * start
        print(mutliple)
        start = start + 1


result = multiplicationTable(8)
