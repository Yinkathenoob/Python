from random import randint


num = randint(0,100)


def guess_num(guess:int):
    
    choose_difficulty = input("Select difficulty: Easy, Medium or Hard ")
    
    if choose_difficulty == "easy":
    
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
            if attempts == 10:
                print("Max number of attempts reached! The game will end now")
                exit()
    
    elif choose_difficulty == "hard":
        guess = int(input("Enter a random number: "))
        should_continue = True
        attempts = 0
                
guess_num(1)





