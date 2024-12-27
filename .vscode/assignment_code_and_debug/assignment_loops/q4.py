def mul(num: int, num1: int) -> int:
    sum = 0
    for i in range(1, 2 * num + 1, 2):
        sum = sum + num ^ i
        i += 1
    print(sum)


mul(6, 4)
