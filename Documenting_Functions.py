def test(a:int, b:int) -> int:
	'''A simple function that prints 2 parameters'''
	print(a)
	print(b,'\n')
	return a + b

test(5,10)
print(test.__doc__) # <-- printa o texto que a gente colocou na função
help(test) # <-- uma versão mais detalhada do test.__doc__