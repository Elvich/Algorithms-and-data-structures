import math

def find_furthest_point(x_coords, y_coords):
    max_distance = -1  
    furthest_point = (0, 0)

    for x, y in zip(x_coords, y_coords):
        if x < 0 and y > 0:
            distance = math.sqrt(x**2 + y**2)
            if distance > max_distance:
                max_distance = distance
                furthest_point = (x, y)

    return furthest_point

x_coords = [-3, 2, -1, -4, 5]
y_coords = [4, -2, 5, 1, -3]

result = find_furthest_point(x_coords, y_coords)
print("Наиболее удаленная точка:", result)