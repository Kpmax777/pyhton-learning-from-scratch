"""
Take 10 integer inputs from user and store them in a list. Now, copy all
the elements in another list but in reverse order
"""


def func(num: list):
    result = []
    for i in range(len(num) - 1, -1, -1):
        result.append(num[i])
    print(result)


input1 = []
for i in range(0, 3):
    data_input = int(input("enter a number:"))

    input1.append(data_input)
print(input1)
func(input1)
