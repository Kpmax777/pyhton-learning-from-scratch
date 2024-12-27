marks: int = int(input("enter marks from student: "))


if marks > 90 and marks < 101:
    print("A")
elif marks > 80 and marks < 91:
    print("B")
elif marks > 70 and marks < 81:
    print("D")
else:
    print("Fail")
