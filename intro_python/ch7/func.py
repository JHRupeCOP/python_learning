#

def wisdom():
    print("Life is like a box of chocolates.")

def fizz_buzz(x):
    if x % 3 == 0 and x % 5 ==0:
        print(f"{x} is FIZZ BUZZ!")
    elif x % 3 == 0:
        print(f"{x} is FIZZ")
    elif x % 5 == 0:
        print(f"{x} is BUZZ")
    else:
        print(f"{x} is boring")

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def namer(first, last):
    print(f"Hello {first} {last}")

wisdom()

fizz_buzz(15)

print(is_even(99))

my_variable = is_even(99)
print(my_variable)

namer("Jim", "Ruppert")
