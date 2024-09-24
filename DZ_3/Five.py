import math

n = int(input("Введите число: "))
x = []
for i in range(0,n):
    x.append(int(input(f"Введи {i+1}-е число вектора X: ")))

y = []
for i in range(0,n):
    y.append(int(input(f"Введи {i+1}-е число вектора Y: ")))

def euclidean_distance(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

min_dist = float('inf')
closest_indices = None

for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean_distance((x[i], y[i]), (x[j], y[j]))

        if dist < min_dist:
            min_dist = dist
            closest_indices = (i, j)

print(min_dist)
for idx in closest_indices:
    print(f"({x[idx]}, {y[idx]})")