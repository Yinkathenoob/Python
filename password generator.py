print(" password generator")
import random
import string

def inputt():
    while True:
        inputt = input(" suggest strong password? ")
        if inputt == "yes":
            return password
            
        else:
                
                print("Thanks")
                exit()
                
                
                  
lower  = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+{}:\"<>?[];',./\\"
all_chars = lower + upper + numbers + symbols

length = int(input('Enter Password Length more than 4: '))
if length < 4:
    print("Select 4 characters and above for a strong password!")
    exit()
else:
    password =' '. join (random.sample(all_chars, length))


inputt()
print ("Generated password: ", password)