from os import system
system("clear")

# ranges start a zero
for num in range(6):
    print(num)

print("\n"*2)

# ranges start at specific number
for num in range(2,10):
    print(num)

print("\n"*2)

for num in range(4):
    print("I love cheese")

print("\n"*2)

# for loop to iterate over a list
names = [ "James", "Remus", "Peter", "Sirius" ]
for name in names:
    print(name)

print("\n"*2)

# iterate of a variable
name = "Jim Ruppert"
for x in name:
    print(x)

print("\n"*2)

# Using else with for
for x in range(3):
    print(x)
else:
    print("All done")

    
print("\n"*2)

# pass statement
# allows for an empty loop
for x in range(3):
    pass

