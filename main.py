menu = {"pizza": 15.00,
        "coca-cola": 3.50,
        "hamburger": 8.00,
        "fanta": 3.50,
        "paper": 0.50,
        "water": 1.00}

cart = []
total = 0

print()
print("-------MENU-------")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f}$")
print("------------------")

while True:
    food = input("Select items from cart (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)

print()
print(f"Total is {total:.2f}$")

