capacity = 100
water = 50
threshold = 80

inflow = [20, 30, 10, 40, 15]
outflow = [10, 15, 20, 10, 5]

for day in range(len(inflow)):
    water += inflow[day] - outflow[day]

    if water > capacity:
        water = capacity
        print(f"Day {day+1}: Overflow")

    elif water < 0:
        water = 0
        print(f"Day {day+1}: Shortage")

    print(f"Day {day+1}: Water level = {water}")

    if water >= threshold:
        print(f"Threshold reached on Day {day+1}")
        break
