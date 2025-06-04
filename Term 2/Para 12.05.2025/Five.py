import numpy as np

def sort_matrix_by_first_column(matrix):
    return matrix[matrix[:, 0].argsort()]



matrix = np.array([
    [5, 2, 3],
    [1, 4, 6],
    [3, 7, 8]
])

print("Упорядоченная матрица:\n", sort_matrix_by_first_column(matrix))