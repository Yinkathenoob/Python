import random
from random import randint


difficulty = input("select difficulty: 1 for easy, 2 for medium, 3 for hard ")
if difficulty == "1":
    num = randint(1,100)
    attempts = 10
elif difficulty == "2":
    num = randint(1,500)
    attempts = 7
elif difficulty == "3":
    num = randint(1,1000)
    attempts = 5
else:
    print("Error, invalid difficulty level")
    exit()



while attempts > 1 :
    guess =int(input("Guess a number "))
    attempts -= 1
    if not guess.__int__ :
        print("Invalid input. Please enter a numeric value.")
        continue

    if guess == num:
            print("You have guessed the correct number!")
            
    elif guess > num:
            print("Your guess is too high")
            
    elif guess < num:
            print("Your guess is too low")
    print(f"{attempts} attempts left")
            

if attempts == 0:
    print(f"sorry, you ran out of attempts. The secret number was {num}. Better luck next time!")

