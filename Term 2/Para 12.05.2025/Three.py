import numpy as np

def zero_below_secondary_diag(A):
    M = A.shape[0]
    indices = np.tri(M, M, k=-1, dtype=bool)
    A[::-1, :] *= ~indices
    A[:] = A[::-1, :]

    return A



A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Матрица после обнуления ниже побочной диагонали:\n", zero_below_secondary_diag(A))