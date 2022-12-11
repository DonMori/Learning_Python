# # x = 5
# # if x > 10:
# # 	print('x is greater than 10')
# # else:
# # 	print('x is NOT greater than 10')

# qntd = 0

# if 'a' in 'banana':
# 	for i in 'banana':
# 		if i == 'a':
# 			qntd+=1
# 	print(qntd)
# else:
# 	print("there's no 'a' in 'banana'")

# money_available = 100

# if money_available >= 80:
# 	print('Eat something fancy')
# elif money_available > 45:
# 	print('Eat something nice')
# elif money_available > 15:
# 	print('Eat something okay')
# else :
# 	print('Eat something cheap')

# num = 10

# se QUALQUER uma das condições for verdadeira o OR vai fazer o IF rodar
# if num != 10 or num > 5:
# 	print(True, '\n'*10)

# money_available = 100
# hungry = False
# bored = True

# if money_available > 80 and hungry == True or bored == True:
# 	print('Eat something fancy!')

# nested if statements


# x = '1'
# if x in ['a', 'b', '1']:
# 	print(f"'{x}' is in the list")
# 	if x.isalpha():
# 		print('it is a letter')

money_available = 100
hungry = True
bored = True

if money_available > 80:
	if hungry:
		if bored:
			print('Eat something fancy!')

