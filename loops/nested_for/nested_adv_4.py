def num(n: int):
    for i in range(1, n // 2 + 2):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    for i in range(n // 2, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


num(15)
