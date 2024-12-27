first = int(input("enter the start point : "))
last = int(input("enter the end point : "))


def list_value(first, last):
    list1 = [1, 3, 6, 7, 3, 45, 32, 56, 132, 32]
    result = []
    for i in list1[first:last]:
        result.append(i)

    return result


c = print(list_value(first, last))
