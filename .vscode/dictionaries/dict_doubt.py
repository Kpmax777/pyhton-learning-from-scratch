my_dict = {"kp": {"fav": "ice_cream"}, "lalli": {"fav": "chacolate"}}
x = my_dict.items()

y = dict(sorted(my_dict.items(), key=lambda x: x[1]["fav"]))
print(y)
