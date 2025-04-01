def fibonacci_squares(N):
    fib = [0, 1]
    for i in range(2, N):
        fib.append(fib[-1] + fib[-2])
    squares = list(map(lambda x: x ** 2, fib[:N]))
    return squares

N = 10
result = fibonacci_squares(N)
print(result)