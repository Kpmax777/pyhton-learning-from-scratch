"""Make a list of your own. Print the whole list in reverse using FOR loop
and WHILE loop."""

a = [12, 5, 48, 7, 24]


for i in range(0, len(a)):

    if a[i] % 3 == 0 and a[i] % 4 == 0:

        print(a[i], end=" ")
