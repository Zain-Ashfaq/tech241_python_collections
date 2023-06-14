
starters = ["Samosa", "Chicken Tikka", "Bread Sticks"]
mains = ["Butter Chicken", "Fish and Chips", "Lamb Biryani"]
desserts = ["Gulab Jamun", "Apple Crumble", "Rasmalai", "Chocolate Brownie", "Vanilla Ice Cream"]

orders = []

print("Menu:")

print("Starters:")

for starter in starters:
    print("-", starter)

print("Mains:")

for main in mains:
    print("-", main)

print("Desserts:")

for dessert in desserts:
    print("-", dessert)


for i in range(3):
    order = input("Enter your order: ").title().strip()
    # print(order)
    # if order in desserts:
    #     print(f"{order} does exist")
    while order not in starters and order not in mains and order not in desserts:
        print("Sorry we dont serve that, please pick another item")
        order = input("Enter your order: ").title().strip()
    orders.append(order)


print("Your Orders:")
for order in orders:
    print("-", order)
