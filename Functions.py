def test_function():
	print('hi!')

def calc_sum(num1, num2):
	print(num1+num2)

def better_calc(num1, num2, op):
	if op == 'plus':
		print(num1+num2)
	elif op == 'minus':
		print(num1-num2)
	else:
		print('Something went wrong')

# test_function()
# calc_sum(5,10)

better_calc(10, 50, 'plus')
better_calc(10, 50, 'minus')