for i in range(5, -1, -1):
    for k in range(5 - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
