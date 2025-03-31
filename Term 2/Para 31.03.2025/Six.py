data = [
    ('Alberto Franco', '15/05/2002', '35kg'),
    ('Gino Mcneill', '17/05/2002', '37kg'),
    ('Ryan Parkes', '16/02/1999', '39kg'),
    ('Eesha Hinton', '25/09/1998', '35kg')
]

names = [item[0] for item in data]
dates = [item[1] for item in data]
weights = [int(item[2][:-2]) for item in data]

print(names)
print(dates)
print(weights)