import numpy as np

def count_columns_with_unique_elements(matrix):
    return np.sum(np.apply_along_axis(lambda col: len(np.unique(col)) == len(col), axis=0, arr=matrix))


A = np.array([
    [1, 2, 3],
    [4, 5, 3],
    [7, 8, 3]
])
print("Количество столбцов с уникальными элементами:", count_columns_with_unique_elements(A))