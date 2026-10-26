import math

points = [(0, 0), (3, 4), (6, 8), (12, 8)]
distances = []

for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    distances.append(d)
    print("Distance:", d)

print("Longest segment:", max(distances))