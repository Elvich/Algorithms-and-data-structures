import random


def create_B_array(A):
    N = len(A)
    B = [0] * N

    suffix_sum = 0
    for k in range(N - 1, -1, -1):
        suffix_sum += A[k]
        B[k] = suffix_sum

    return B

A = [random.randint(1,10) for i in range(random.randint(1,10))]
B = create_B_array(A)
print("Массив A:", A)
print("Массив B:", B)