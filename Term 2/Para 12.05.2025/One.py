import numpy as np

def sum_parallel_diagonals(A):
    M = A.shape[0]
    result = []

    for d in range(1 - M, M):
        diag = np.diagonal(A, offset=d)
        result.append(np.sum(diag))

    return result



A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Суммы диагоналей, параллельных главной:", sum_parallel_diagonals(A))