# the input should be divisible 2 or 3 but not 8:

num: int = int(input("enter number : "))
if (num % 2 == 0 or num % 3 == 0) and num % 8 != 0:
    print("divisible by the 2 and 3")
else:
    print("can't be divisible by the number")
