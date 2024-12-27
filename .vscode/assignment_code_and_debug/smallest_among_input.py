# smallest along the given number
"""
c = []
for x in range(5):
    c.append(0)"""

number = []

for i in range(0, 4):
    num = input("enter a number:")
    number.append(num)
print(number)

var = number[0]

if int(number[1]) < int(var):
    var = number[1]
if int(number[2]) < int(var):
    var = number[2]
if int(number[3]) < int(var):
    var = number[3]
print("smallest number among the list ", var)
