import numpy as np

def count_similar_rows(matrix):
    
    first_set = set(matrix[0])
    count = 0

    for row in matrix:
        if set(row) == first_set:
            count += 1

    return count



matrix = np.random.randint(0, 5, size=(5, 4))
print("Матрица:\n", matrix)
print("Количество строк, похожих на первую:", count_similar_rows(matrix))