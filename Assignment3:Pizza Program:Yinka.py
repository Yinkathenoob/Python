#SP= small pizza price, MP= medium pizza price, LP= large pizza price, PSP= pepperoni for small pizza, PMLP= pepperoni for medium/large pizza, EC= extra cheese
SP = 15
MP = 20
LP = 25
PSP = 2
PMLP = 3
EC = 1

#taking inputs from the user
size = input("What size of pizza would you like to order? (S for small ($15), M for medium($20), L for large ($25)): ").upper()
add_pepperoni = input("Would you like pepperoni with your order?(costs $2 for small pizzas and $3 for medium and large pizzas) (Y for yes, N for no): ").upper()
extra_cheese = input("Do you want extra cheese on your pizza? (Y for yes, N for no): ").upper()


#Calculate size pricing based on input received from user, returns error message in case of invlid input
if size == "S":
    pizza_price = SP
elif size == "M":
    pizza_price = MP
elif size == "L":
    pizza_price = LP
else:
    print("Invalid pizza size, please select S, M, or L.")
    exit()


#Calculate pepperoni price depending on if user opts for it and pizza size 
if add_pepperoni == "Y":
    if size == "S":
        pizza_price += PSP
    elif size == "M" or "L":
        pizza_price += PMLP


#Add extra cheese price to total if user opts for it
if extra_cheese == "Y":
    pizza_price += EC


#return final bill
print(f"Your total bill is ${pizza_price}")