menu = {
    'pasta': 200,
    'coffee': 120,
    'sandwitch': 150,
    'pizza': 250,
    'salad': 80
}

print("Welcome to the Cafe Management System")
print("pizza: Rs250\nPasta: Rs200\nCoffee: Rs120\nSalad: Rs80\nSandwitch: Rs150")

Order_total = 0

# First Order
item_1 = input("Enter the name of the item you want to order: ")
if item_1 in menu:
    Order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Order item '{item_1}' is not available yet!")

# Second Order Option
another_order = input("Do you want to order another item? (Yes/No): ")

if another_order.lower() == "yes":  # Proper method call
    item_2 = input("Enter the name of the second item: ")
    if item_2 in menu:
        Order_total += menu[item_2]
        print(f"Item '{item_2}' has been added to your order.")
    else:
        print(f"Order item '{item_2}' is not available yet!")

# Final Bill
print(f"The total amount to pay for your order is: Rs{Order_total}")
