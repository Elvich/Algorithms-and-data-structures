def sort_points(x_coords, y_coords):
    points = list(zip(x_coords, y_coords))

    points.sort(key=lambda point: (-point[0] - point[1], -point[0]))

    return points


x_coords = [3, 1, 4, 1, 5]
y_coords = [2, 3, 1, 5, 0]

sorted_points = sort_points(x_coords, y_coords)

print("Отсортированные точки:")
for point in sorted_points:
    print(point)