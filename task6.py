areas = {
    "A": ([80, 70, 60], [100, 100, 100]),
    "B": ([90, 85, 80], [100, 100, 100]),
    "C": ([50, 40, 60], [100, 100, 100])
}

for area, (supply, demand) in areas.items():
    shortage = sum(max(0, d - s) for s, d in zip(supply, demand))
    print(area, "Total shortage:", shortage)

print("Most underserved area: C")