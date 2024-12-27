my_dist = {"kp": 71, "lalli": 72}

key_name = input("enter a name: ")

x = my_dist.get(key_name)

if x is not None:
    print(x)
else:
    print("wrong Key")
