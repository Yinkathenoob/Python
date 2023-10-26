def pal(word):
    word = input("Enter a word")
    if word[::-1] == word:
        print("It is a palindrome")
    else: print("it is not a palindrome")

pal("yinka")