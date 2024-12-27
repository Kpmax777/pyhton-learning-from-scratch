from typing import List


def even_odd(num: int):
    output = []
    for i in range(0, len(num)):
        if num[i] % 2 == 0:
            output[i] =  + 1

        else:
            output[i] = output[i] + 1


list1: List[int] = [21, 22, 34, 56, 55, 23]


print(even_odd(list1))
print(list1)
