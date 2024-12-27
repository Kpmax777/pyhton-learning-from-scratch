def is_prime(num: int) -> bool:
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False


my_list = [i for i in range(1, 101) if is_prime(i) == True]

print(my_list)
