n = 10
fib = lambda x: fib(x - 1) + fib(x - 2) if x > 1 else x
fibonacci_series = [fib(i) for i in range(n)]
print("Ряд Фибоначчи:", fibonacci_series)
print()

from itertools import permutations

next_permutation = lambda num: min(
    (int("".join(p)) for p in permutations(str(num)) if int("".join(p)) > num),
    default=False
)

print(next_permutation(12))
print(next_permutation(10))
print(next_permutation(201))
print(next_permutation(102))
print(next_permutation(445))
print()

words = ['red', 'black', 'white', 'green', 'orange']
substring = 'ack'
result = list(filter(lambda x: substring in x, words))
print("Строки, содержащие подстроку '{}':".format(substring), result)