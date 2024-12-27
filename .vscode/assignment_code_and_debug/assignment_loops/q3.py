def que(num: int, num1: int) -> int:
    sum = 0
    for i in range(1, 2 * num1 + 1, 2):
        sum = sum + num / i
        i += 1
    print(sum)


que(6, 4)
que(9, 11)
