# Shopping cart list starts empty
cart = []

# Adding items to the cart
def add_to_cart(item, cost):
    cart.append((item, cost))

# Calculate total cost
def calculate_total_cost(cart):
    total_cost = sum(cost for _, cost in cart)
    return total_cost

# Applying discounts
def apply_discounts(total_cost):
    if total_cost >= 100:
        return total_cost * 0.9  # 10% discount for orders over $100
    elif total_cost >= 50:
        return total_cost * 0.95  # 5% discount for orders over $50
    else:
        return total_cost

# Main shopping cart loop
while True:
    item = input("Enter the item name (or type 'checkout' to complete your purchase): ")
    
    if item.lower() == 'checkout':
        total_cost = calculate_total_cost(cart)
        final_cost = apply_discounts(total_cost)
        print(f"Total cost: ${total_cost:.2f}")
        print(f"Final cost after applying discounts: ${final_cost:.2f}")
        break
    
    cost = float(input("Enter the cost of the item: $"))
    add_to_cart(item, cost)
