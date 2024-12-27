def num(n1: int, n2: int) -> int:

    i = 1
    total = 0
    while i <= n1:
        if i % n2 == 0:
            total = total + i
    i = i + 1
    return total


r = num(64, 3)
print(r)


"""
def func(num1:int, num2:int)->int:
    i=1
    sum=0
    while i<=num1:
        if i%num2==0:
            sum=sum+num1
            print(i)
        i+=1
    return sum

sum=func(64,3)
print(sum)


"""
