# Write a program that takes two numbers as input and checks if the first
# number is divisible by the second.

num1 = int(input("enter number num1: "))
num2 = int(input("enter number num2: "))

if num1 / num2 == 0:
    print("divisible")
else:
    print("not divisible")
