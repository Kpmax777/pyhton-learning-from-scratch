student: str = input("enter the student input (yes/no):")

if student == "yes":
    class_attended: int = int(input("enter no class attended: "))
    if class_attended > 20:
        assignment_submited: int = int(input("enter no of assignment submitted: "))

        if assignment_submited > 45:
            print("certification completd")
        else:
            print("not eligible for certificate")
    else:
        print("class_attendance low")
else:
    print("not part of C and d")
