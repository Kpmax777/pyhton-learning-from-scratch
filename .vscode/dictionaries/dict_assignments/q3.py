"""
. Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the name of the subject which has marks
more than passing marks (above 33).

"""

kp = {"chemistry": 33, "maths": 94, "physics": 91, "science": 101}
max = 0
subject = " "
for keys, values in kp.items():

    if values > 33:
        subject = keys
        max = values

    print(subject)
