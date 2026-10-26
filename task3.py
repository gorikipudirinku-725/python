weight = float(input("Enter parcel weight (kg): "))
distance = int(input("Enter distance (km): "))
urgent = input("Urgent delivery? (yes/no): ")

charge = weight * 10 + distance * 2

if urgent == "yes":
    charge += 100

if weight > 20:
    print("Parcel not eligible")
else:
    print("Delivery charge: ₹", charge)
    print("Service: Express" if urgent == "yes" else "Standard")