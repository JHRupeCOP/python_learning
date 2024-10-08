from os import system

system("clear")

'''
Create a List with the names of five people you know and output
the second name to the screen.
'''
names = [ "Jim", "Angie", "Anthony", "Emily", "Hailey" ]
print(names)
print(names[1])


'''
Create a List where the first item in the List is a math problem,
like 1 + 1 and the rest of the items are names. Output the first item
to the screen. (WOAH, MATH can be an item in a List?!)
'''
things = [ 2+3, "Sam", "Alec", "Ben" ]
print(things)
print(things[0])


'''
Create a multi‐dimensional List with 4 items, and each item is
itself a List containing a personʹs name, their address, and phone
number (make up the info). Output the second item in your
multidimensional List.
'''
people = [ ["Harry", "Under the stairs", "+44 01 12485"], ["Ron", "the Burrow", "+44 01 34949"], ["Luna", "the Black Tower", "+44 01 93843"], ["Snape", "Hogwarts", "+44 03 98432"]]
print(people)
print(people[1])

'''
Output just the phone number of the third item in your List from
the last question.
'''
print(people[2][2])
