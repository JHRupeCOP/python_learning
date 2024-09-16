
# Basic if statements
x = 41
if x == 42:
    print("X does equal 41")
else:
    print("X does not equal 41")


name = "Ralph"
if name == "Bob":
    print("Hi Bob")
elif name == "John":
    print("How do John")
else:
    print("I don't know you")

'''
AND or OR
AND: to evaluate to true both sides must be true
OR: to evaluate to true only 1 side needs to be true
'''

name = input("Enter your name: ")
if name == "John" or name == "Bob":
    print(f"Hi {name}")
else:
    print("Be gone straner")


