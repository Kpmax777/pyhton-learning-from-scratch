def num(n: int):
    number: int = 1
    i = 1
    while i <= number:
        print(number, end=" ")
        if i % 2 == 0:
            number = number + 2

        else:
            number = number + 3
            print(number)

        i = i + 1


num(6)
