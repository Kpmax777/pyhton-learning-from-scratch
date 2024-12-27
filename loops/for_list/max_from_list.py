from typing import List


def maxList(a: int):
    largest = a[0]
    for i in range(0, len(a)):

        if largest > a[i]:

            largest = a[i]
    return largest


numbers: List[int] = [10, 7, 8, 10, 11]

result = maxList(numbers)
print(result)
