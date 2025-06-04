import numpy as np

def invert_local_maxima(matrix):
    matrix = np.array(matrix)
    padded = np.pad(matrix, pad_width=1, mode='edge')
    result = matrix.copy()

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            neighbors = padded[i:i+3, j:j+3]
            if matrix[i, j] == np.max(neighbors) and np.count_nonzero(neighbors == matrix[i, j]) == 1:
                result[i, j] *= -1

    return result


C = np.array([
    [1, 3, 2],
    [4, 9, 5],
    [6, 7, 8]
])
print("Матрица после изменения локальных максимумов:\n", invert_local_maxima(C))