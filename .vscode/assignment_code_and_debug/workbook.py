man = []
sum = 0
for i in range(0, 3):
    num = int(input("enter three number:"))
    man.append(num)
    sum = sum + man[i]

avg = sum / len(man)
print(avg)
