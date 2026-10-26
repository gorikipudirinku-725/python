balance = 1000
transactions = ["deposit 500", "withdraw 200",
                "withdraw 200", "withdraw 200"]

for t in transactions:
    action, amount = t.split()
    amount = int(amount)

    if action == "deposit":
        balance += amount
    elif amount <= balance:
        balance -= amount
    else:
        print("Invalid withdrawal")

print("Final balance:", balance)

if transactions.count("withdraw 200") > 1:
    print("Suspicious repeated transactions")