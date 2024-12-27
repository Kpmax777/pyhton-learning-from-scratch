"""

i = 1

k: int = int(input("enter a number: "))
while i <= k:
    print(i)
    i = i + 1 """


def printPattern(n: int) -> None:
    i: int = 1
    while i <= n:
        print(i, end=" ")
        i = i + 1
    print()


printPattern(10)
printPattern(5)
printPattern(47)
