from random import randint



num = randint(0,100)
attempts =0

def guess_num(guess:int):
    guess = int(input("Enter a random number: "))
    should_continue = True

    while should_continue:
        attempts+=1
        if guess == num:
            print("You have guessed the correct number!")
            should_continue = False
        elif guess > num:
            print("Your guess is too high")
            continue
        elif guess < num:
            print("Your guess is too low")
        continue
guess_num(3)
