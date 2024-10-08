from os import system
system("clear")
# intro to lists

# Create the list
names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]
# print the list
print(names)
# print the conents of the thirs position (first is 0)
print(names[2])

var_1 = "Tim"
# when using a variable or integer no qoutes
names_1 = ["John", var_1, "Mary", 41, "Bluto"]
print(names_1)
print(names_1[1])

print(len(names))
print(len(names_1))

names_2 = ["John", "April"]
print(len(names_2))
# add a single element to the lit
names_2.append("Bob")
print(names_2)
print(len(names_2))

# instert an item in a specific location
names_2.insert(0, "Lily")
print(names_2)
print(len(names_2))

# add multiple items to the list
names_2.extend(["James", "Remus"])
print(names_2)
print(len(names_2))

# remove a named item from the list
# if multiple items with the same name only the first occurance is removed
names_2.remove("Bob")
print(names_2)
print(len(names_2))

# remove a specific postion from the list
names_2.pop(1)
print(names_2)
print(len(names_2))

