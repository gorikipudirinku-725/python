participants = ["A", "B", "C", "A"]
fees = 4 * 100
sponsorship = 500
expenses = 200

unique = set(participants)
duplicates = len(participants) - len(unique)
balance = len(unique) * 100 + sponsorship - expenses

print("Unique participants:", len(unique))
print("Duplicate registrations:", duplicates)
print("Final balance: ₹", balance)