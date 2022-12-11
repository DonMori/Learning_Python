inventory_names = ['Screws', 'Wheels', 'Metal parts', 'Rubber bits', 'Screwdrivers', 'Wood']
inventory_numbers = [43, 12, 95, 421, 23, 43]

# print(zip(inventory_names, inventory_numbers))
# print(list(zip(inventory_names, inventory_numbers)))

# for name, number in zip(inventory_names, inventory_numbers):
# 	# print(inv_object)
# 	# print(inv_quantity)
# 	print(f'{name} current inventory: {number}')


# Enumerate function - get the current index, which is VERY GOOD

# print(list(enumerate(inventory_names)))
# for index, name in enumerate(inventory_names):
# 	print(f'{index}: {name}')
# 	if index == len(inventory_names) // 2:
# 		print("Halfway done!")


# coisas importantes :
# enumerate fala quais são os índices de itens da lista
# lista = ['a', 'b', 'c']
# print(list(enumerate(lista)))
# então o valor 'a' está no índice 0
# o valor 'b' está no índice 1
# e assim por conseguinte

# for index, name in enumerate(inventory_names):
# 	print(f'{index}: {name}')
# 	if index == len(inventory_names) // 2:
# 		print('Halfway there!')

# Exercise

# combinar zip e enumerate

for index, inventory_tuple in enumerate(zip(inventory_names, inventory_numbers)):
	print(f'{inventory_tuple[0]} [id: {index}] - inventory: {inventory_tuple[1]}')






















