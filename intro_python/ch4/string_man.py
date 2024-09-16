# string manipulation
'''
lower() Convert to all lowercase
upper() Convert to all uppercase
capitalize() Capitalize just first letter
title() Capitalizes first letter of each word swapcase() Switches capitalized to lowercase & vice versa len() *Returns character length
rstrip() Removes trailing spaces
'''


name = input("Enter your name: ")
print(f"Hi there {name.lower()}")

# or assign upper to variable 
name = name.upper()
print(name)

# len function
print(f"The name {name} has {len(name)} characters.")

phrase = input("Enter a phrase: ")
print(f'You entered: {phrase}!')
print(f'<{phrase.capitalize()}>')
print(f'<{phrase.title()}>')
print(f'<{phrase.rstrip()}>')


