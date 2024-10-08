from os import system
system("clear")

#multi-dimensional lists

names = [ "James", "Sirius", "Remus", "Peter", [1, 2, 3, 4]]
print(len(names))
print(names)

# access the embedded list
print(names[4][2])

numbers = [1,2,3,4]
names = [ "James", "Sirius", "Remus", "Peter", numbers ]
print(len(names))
print(names)
