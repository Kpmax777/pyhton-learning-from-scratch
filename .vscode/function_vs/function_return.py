def add(num1, num2, num3) -> int:
    total = num1 + num2 + num3

    return total


def evenOrOdd(total: int) -> None:
    if total % 2 == 0:
        print("Even")
    else:
        print("odd")


t = add(24, 34, 54)
print(t)
evenOrOdd(t)
