def decode(message):
    message = input("Enter your encoded message: ")
    reversed_message = message[::-1]
    final_message = "".join([i for i in reversed_message if i.isalpha()])
    print(final_message)


decode("")