from random import randint

'''
Create a simple math flashcard game that asks a user what two numbers added together equal and tell them whether or not they got the answer correct.
'''

num_1 = randint(1, 10)
num_2 = randint(1, 10)
sum_numbers = num_1 + num_2

answer_sum = int(input(f'What is the sum of {num_1} and {num_2}: '))

if answer_sum == sum_numbers:
    print("Correct")
else:
    print(f'Sorry you are wrong, the correct answer is {sum_numbers}')


'''
Write some code that asks for a personʹs full name (first and last name) and then output their name with both first and last name capitalized
'''
full_name = input("Enter your first and last name: ")
print(full_name.title())

'''
Write some code that asks for a personʹs name and then tell that person how many characters are in their name (added them up manually yourself to see if the answer is correct!)
'''
first_name = input("What is your first name: ")
print(f"Your first name has {len(first_name)} characters")
