"""
Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the highest marks scored.
"""

kp = {"chemistry": 89, "maths": 94, "physics": 91, "science": 100}
max = 0
for values in kp.values():

    if values > max:

        max = values

print(f" max marks :{max}")
