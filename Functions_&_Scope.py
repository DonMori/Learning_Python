'''
Variables created inside of a function
are only available inside of that function

This is called a 'local Scope'
Creating variables outside of functions
is the 'global scope'

Example
'''

# a = 15

# def test_func():
# 	print(a)

# test_func()
# this works because a is a global function

# def test_func_local():
# 	a+=2
# 	print(a)

# test_func_local()

# def test_func_local():
# 	a = 200
# 	print(a) # essa variável 'a' só existe dentro dessa função

# test_func_local()

# This happens because some words might repeat
# and we can use them again without refering to the last variable
# like capacity in a battery or in a tank
# you can use the variable capacity without capacity_tank and capacity_battery

# Sumarizing : Local scopes inside of a function
# helps us to keep things organised

# Global variables can be accessed in the local scope
# but they cannot be changed (or created)

#               V- pega a variável global
# def test_func_3(a):
# 	value = a+10
# 	return value

# a = 10
# print(test_func_3(a))

multiplier = 3
has_calculated = False
#						  V-- valor a ser multiplicado
def multiply_calculator(number):
	global has_calculated
	result = number * multiplier
	has_calculated = True
	return result # Return ends the function call
				  # It's like a break 

print(multiply_calculator(5)); print(has_calculated)




