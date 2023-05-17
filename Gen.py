def flat_generator(nested_list):
    for i in nested_list:
        yield i

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

flat_list = [el for item in flat_generator(nested_list) for el in item]
print(flat_list)
