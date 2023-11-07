data = [1, 5.8, 3.0, 4]

integer_data = list(filter(lambda numer: isinstance(numer, int), data))

print(integer_data)
