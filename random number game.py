from random import randint



num = randint(0,100)


def guess_num(guess:int):
    guess = int(input("Enter a random number: "))
    should_continue = True
    attempts = 0

    while should_continue:
        attempts += 1

        print(f"Number of attempts: ", attempts)
        if guess == num:
            print("You have guessed the correct number!")
            should_continue = False
        elif guess > num:
            print("Your guess is too high")
            guess_num(1)
        elif guess < num:
            print("Your guess is too low")
            guess_num(1)
guess_num(1)







