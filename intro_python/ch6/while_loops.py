from os import system
system("clear")


num = 0
while num < 10:
    print(num)
    num += 1

print("\n"*2)

num = 0
while num < 10:
    num += 1
    if num == 5:
        break
    print(num)

print("\n"*2)
num = 0
while num < 10:
    num += 1
    if num == 5:
        continue
    print(num)

