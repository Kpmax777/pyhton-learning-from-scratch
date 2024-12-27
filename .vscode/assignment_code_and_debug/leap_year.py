# leap year

y: int = int(input("enter a year: "))

if y % 4 == 0:
    print("leap year")
elif y % 4 == 0 and y % 100 == 0:
    print("not a leap year")
elif y % 4 == 0 and y % 400 == 00:
    print("leap year")
else:
    print("not a leap year")
