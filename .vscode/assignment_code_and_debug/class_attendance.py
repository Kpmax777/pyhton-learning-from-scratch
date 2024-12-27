# class attendance

working_days: int = int(input("no.of working days: "))
attend_days: int = int(input("no of attend days: "))

overall_percentage = (attend_days / working_days) * 100
print(int(overall_percentage))

if overall_percentage > 75:
    print("good student")
else:
    print("he cannot attend sit in exam")
