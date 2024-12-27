"""
Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the name of the subject with highest marks
scored.
"""

# from types import Dict:


kp = {"chemistry": 89, "maths": 94, "physics": 91, "science": 101}
max = 0
subject = " "
for keys, values in kp.items():

    if values > max:
        subject = keys
        max = values

print(f" max marks :{subject} {max}")
