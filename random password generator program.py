import random
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','&','+','?']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("welcome to the password genrator!\n")

numofletters = int(input("How many letters would you like to be in your password?\n"))
numofsymbols = int(input("How many symbols would you like to be in your password?\n"))
numofnumbers = int(input("How many numbers would you like to be in your password?\n"))

pass_list = []
for char in range(1, numofletters +1):
    pass_list += random.choice(letters)

for char in range(1, numofsymbols +1):
    pass_list += random.choice(symbols)

for char in range(1, numofnumbers +1):
    pass_list += random.choice(numbers)

random.shuffle(pass_list)

password = ""

for i in pass_list:
    password += i


print("Your randomly generated password is: ", password)