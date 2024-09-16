print("Write some code that outputs your name to the screen")
first_name = input("What is your first name: ")
print(f"Your name is: {first_name}")

print('\n' * 2)
print("Write some code that outputs your name to the screen 10 times using math")
print(first_name  * 10)

print('\n' * 2)
print("Write some code that asks how many Apples youʹd like to purchase and then outputs the response")
num_apples = input("How many apples would you like to buy: ")
print(f"You want {num_apples} apples")  


print('\n' * 2)
print(f'Write some code that asks for a personʹs first name on one line, then after they type it in, asks for their last name. Then tells them "Hello first last name"')
last_name = input("What is your last name: ")
print(f'Hello {first_name} {last_name}')

print('\n' * 2)
print('Write some code that asks (one line at a time) what your name is, where you live, what your phone number is, and what your favorite color is; then outputs all that info to the screen one item per line.')
location = input("Where do you live: ")
phone = input("what is your phone number: ")
fav_color = input("what is your favorit color; ")
print(f'First name: {first_name}\nLast name: {last_name}\nAddress: {location}\nPhone number: {phone}\nFavorite color: {fav_color}')
