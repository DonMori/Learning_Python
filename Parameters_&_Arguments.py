# def test_function(arg1,arg2,arg3,arg4):
# 	print(arg1)
# 	print(arg2)
# 	print(arg3)
# 	print(arg4)

# # test_function(['l', 0, 'L'], 1, True, 'Hello!')
# # Is the same as
# #   test_function(arg4 = ['l', 0, 'L'], arg3 = 1, arg2 = True, arg1 = 'Hello!')

# # Exercise

# def greeter(person = 'Person', greet = 'Hello', weekday = 'Monday'):
# 	print(f'{greet} {person}, today is {weekday}!')

# greeter()
# greeter('Bob', weekday = 'Tuesday', greet = 'Welcome')	

# def print_all(arguments):
# 	# Print all arguments
# 	for argument in arguments:
# 		print(argument, end=" ")

# print_all([1,2,3,4,5,6,7])

# list unpacking
# def print_all(first_argument, *arguments, extra = 'Mouse'): # por causa da * antes do arguments, o python entende que podem ter vários argumentos e ele aceita todos
# 	print(first_argument)
# 	print(arguments)
# 	print(extra)
# 	# for argument in arguments:
# 	# 	print(argument)

first_num = 59
text = 'Big shot!'
test_list = [1,2,3,4,5, ['a', 'b', 'c']]
test_tuple = ('Horse!')
test_set = {'Morrison', 'Ovatsu', 'Miguelos'}

# print_all(first_num, text, test_list, test_tuple, test_set, extra = 'Mouse')
#		  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# então aqui a gente pode ter um monte de coisa

# ----------------------------------------

# Keyword unpacking
# def print_more(**arguments):
# 	print(arguments)

# print_more(arg = '1', arg2 = 'test', arg3 = ['Very', 'Awesome', 'List!'])

# def print_even_more(*args, **kwargs):
# 	print(args) # Cria uma Tupla com tudo
# 	print(kwargs) # Cria um dicionário só com as coisas que o Python detecta que podem ser dicionários (tem chave e valor dentro)

# print_even_more(123, 435, 7182, 'abóbora', 'Cinza', False, 'Marcelo', test = 1, test2 = 10)

# Exercise

def even_better_calc(*nums):
	resul = sum(nums); print(resul) # <-- Achei isso genial
	# resul = 0
	# for num in nums:
	# 	resul += num
	# print(resul)

even_better_calc(123, 456, 1000, 6000)









