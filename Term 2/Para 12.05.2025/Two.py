import numpy as np

def rotate_clockwise_inplace(A):
    M = A.shape[0]


    for i in range(M):
        for j in range(i + 1, M):
            A[i, j], A[j, i] = A[j, i], A[i, j]


    A[:] = A[:, ::-1]




A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

rotate_clockwise_inplace(A)
print("Матрица после поворота на 90° по часовой:\n", A)