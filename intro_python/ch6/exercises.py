'''
Create a multi‐dimensional List with 4 items, and each item is
itself a List containing a personʹs name, their address, and phone
number (make up the info). Loop through the List and output just
each personʹs phone number.
'''
# sample
x = [ ['0,0', '0,1'], ['1,0', '1,1'], ['2,0', '2,1'] ]
for i in range(len(x)):
     for j in range(len(x[i])):
         print(x[i][j])

people = [ ["Harry", "Under the stairs", "+44 01 12485"], ["Ron", "the Burrow", "+44 01 34949"], ["Luna", "the Black Tower", "+44 01 93843"], ["Snape", "Hogwarts", "+44 03 98432"]]

for i in range(len(people)):
    print(people[i][2])

'''
Loop through the List from exercise 2 and print out the full
information of even items in the List (ie the 2nd and 4th List in your
multidimensional List).
'''
x = 1
for i in range(len(people)):
    if x % 2 == 0:
        print(people[i])
    x += 1


