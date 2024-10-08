'''
Print out every number between 1 and 100, one
number per line, but if the number is divisible by three, print out ʺFizzʺ ;
if the number is divisible by five, print out ʺBuzzʺ ; and if the number is
divisible by both three AND five, print out FIZZ BUZZ.
'''

for x in range(1, 101):
    if x % 3 == 0:
        resp_f = "Fizz "
    else:
        resp_f = ""
    if x % 5 == 0:
        resp_b = "Buzz"
    else:
        resp_b = ""
    response = resp_f + resp_b
    if len(response) > 0:
        print(f"{x} - {response}")
    else:
        print(x)


# solution
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print(f"{x} FIZZ BUZZ!")
    elif x % 3 == 0:
        print(f"{x} FIZZ")
    elif x % 5 == 0:
        print(f"{x} BUZZ")
    else:
        print(x)
