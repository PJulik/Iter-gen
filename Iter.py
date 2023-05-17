class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        self.counter = -1
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == len(self.nested_list):
            raise StopIteration
        item = self.nested_list[self.counter]
        return item

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]
for item in FlatIterator(nested_list):
    for el in item:
        print(el)

flat_list = [el for item in FlatIterator(nested_list) for el in item]
print(flat_list)




