#Creating the message decoder as a function
def decode():

    #Taking encoded message as input from the user
    message = input("Enter your encoded message: ")

    #flippping the message around
    reversed_message = message[::-1]

    #Initialize the final message as nothing ("") then add characters which are alphabets or spaces
    final_message = "".join([i for i in reversed_message if i.isalpha() or i.isspace()])

    #Display the final, decoded message
    print("The encoded message is: ", final_message)

#Finally, call the function
decode()



