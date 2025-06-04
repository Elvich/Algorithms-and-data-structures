import numpy as np

def find_saddle_point(matrix):
    matrix = np.array(matrix)
    row_max = np.max(matrix, axis=1)
    col_min = np.min(matrix, axis=0)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] == row_max[i] and matrix[i, j] == col_min[j]:
                return matrix[i, j]

    return 0


B = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
])
print("Седловая точка:", find_saddle_point(B))