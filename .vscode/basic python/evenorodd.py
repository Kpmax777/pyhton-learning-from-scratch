num: int = int(input("Enter a number= "))

if num % 3 == 0 and num % 5 == 0:
    print("FooBar")
elif num % 3 == 0:
    print("foo")
elif num % 5 == 0:
    print("bar")
else:
    print("foofoobarbar")
