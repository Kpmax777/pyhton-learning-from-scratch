Input = ["a", "a", "b", "c", "d", "b", "c", "e", "g", "d", "a", "e"]
# Output: a,"b,c,d,e,g

output = []
for i in input:
    output = output + i
print(output)
