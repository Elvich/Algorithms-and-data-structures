words = ['hello', 'world', 'python', 'lambda', 'function', 'string']
result = list(filter(lambda x: len(x) == 6, words))
print(result)
print()

data = ['Python', 3, 2, 4, 5, 'version']
max_value = max(filter(lambda x: isinstance(x, (int, float)), data))
print(max_value)
print()

data = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
result = list(filter(lambda x: x is not None, data))
print(result)