def convert_and_unique(sequence):
    result = set(map(lambda x: (x.upper(), x.lower()), sequence))
    return result

sequence = ['a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a']
output = convert_and_unique(sequence)
print(output)