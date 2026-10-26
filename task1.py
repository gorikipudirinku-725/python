n = int(input("Enter number of products: "))
total = 0

for i in range(n):
    name = input("Product name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    category = input("Category (food/other): ").lower()

    amount = price * qty

    if qty >= 5:
        amount *= 0.90

    discount = min(amount * 0.05, 100)
    amount -= discount

    tax = 0.05 if category == "food" else 0.18
    amount += amount * tax

    print(name, "Final Amount:", round(amount, 2))
    total += amount

print("Total Bill:", round(total, 2))