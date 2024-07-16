#Start with an empty list
numbers = []

#Take user input of 5 numbers as integer data type
num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))
num3 = int(input("What is the third number? "))
num4 = int(input("What is the fourth number? "))
num5 = int(input("What is the fifth number? "))

#Add all the numbers taken as user input to our empty list using the append function
numbers.append(num1)
numbers.append(num2)
numbers.append(num3)
numbers.append(num4)
numbers.append(num5)
               
#Getting the maximum and minimum numbers from the list
lnum = max(numbers)
snum = min(numbers)

#Display the maximum and minimum numbers
print("Largest number is: ", lnum, "Smallest number is: ", snum)
