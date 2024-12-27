"""
. Create a function that takes three numbers as parameters and returns
the largest among them. Also if no arguments are passed, make sure the
parameters take default value as None and return answer as -1.

"""


def fun(x=None, y=None, z=None) -> int:
    if x != None and y != None and z != None:
        if x > y and x > z:
            return x
        elif y > x and y > z:
            return y
        else:
            return z
    else:
        return -1


x = fun(6, 10, 11)
print(x)


fun(7, 10, 11)
