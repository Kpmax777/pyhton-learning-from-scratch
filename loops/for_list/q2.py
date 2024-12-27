a = [1, 6, 7, 4, 8, 3, 6, 97, 71, 100]

sum_even = 0
sum_odd = 0
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        sum_even = sum_even + a[i]
    else:

        sum_odd = sum_odd + a[i]

print(f"sum of even values: {sum_even}", end=" ")
print()
print(f"sum of odd values: {sum_odd}", end=" ")
