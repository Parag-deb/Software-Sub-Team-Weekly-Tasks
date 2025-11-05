menu = {
    "Burger": 55,
    "Pizza": 50,
    "Pasta": 30,
    "Coffee": 40,
    "Juice": 30,
    "Sandwich": 45,
    "Shawarma": 55,
    "Chicken roll": 35,
    "Puding": 35,
    "Cake": 25,
    "Cha": 10
}

print("Our Menu:")
for item, price in menu.items():
    print(f"{item}: {price} Taka")


# here i'm taking the order/orders
total = 0
order_list = {}
while True:
    order = input("\nEnter item name (or 'done' to finish): ").capitalize()
    
    if order == "Done":
        break
    elif order in menu:
        quantity = int(input(f"How many {order}s would you like? "))
        total += menu[order] * quantity
        #creating order list
        if order in order_list:
            order_list[order] += quantity
        else: order_list[order] = quantity

    else:
        print("Sorry, item not available!")


#showing the order list
print("\nHere is your order list:")
for item, quantity in order_list.items():
    print(f"{item}: {quantity} x {menu[item]} Taka = {quantity * menu[item]} Taka")


# Calculating the bill and discounts
print("\n")
print(f"Total amount: {total} Taka")

if total >= 150:
    discount = total * 0.15
    print("Discount applied: 15%")
elif total >= 120:
    discount = total * 0.10
    print("Discount applied: 10%")
elif total >= 100:
    discount = total * 0.05
    print("Discount applied: 5%")
else:
    discount = 0
    print("No discount applied")

final_amount = total - discount


print(f"Discount amount: {discount:.2f} Taka")
print(f"Final payable: {final_amount:.2f} Taka")

print("Thank you for visiting my Restaurant!")