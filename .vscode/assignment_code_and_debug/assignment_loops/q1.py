def series(num: int) -> int:
    logic: int = 2
    for i in range(1, num + 1):
        print(logic, end=" ")
        logic = (logic * 10) + 2
        i = i + 1
    print()


series(10)
