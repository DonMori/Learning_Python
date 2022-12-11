# # THIS IS SO USEFUL
# # Exemplo usando FOR
# nums_list = [1,3,5,7,9]
# i = 5

# for x in nums_list: print(x, end=" ")
# print('\n')
# # Exemplo usando IF

# if i == nums_list[2]: print(i)
# print('\n')
# # Exemplo usando While

# while i > 0: i = i-1; print(i, end=" ")
# # print('\n')

"""
Example of Ternary operator
x = 5
if x<5:
	color = 'blue'
else:
	color = 'red'

One better way to do it :
if x<5: color = 'blue'
else: color = 'red'

or an EVEN BETTER way to do it

color = 'blue' if x<5 else 'red'
"""

# better way to use match and case

# grade = 1

# match grade:
# 	case 1: print('Very good!')
# 	case 2: print('Good!')
# 	case 3: print("That's a reasonable grade!")
# 	case 4: print('Bad!')		
# 	case 5: print('Very bad!')
# 	case _: print('You... You have no grades? Or wait, did you insert a valid grade?')

# This is a lot more readable than the last one with identations

# Ternary Operator

# x = 2.5
# COR = 'red' SE X>5
# color = 'red' if x>5 else 'blue'; print(color)
#                    else, cor = 'blue'
# print(color)

# ^ ISSO É MUITO DAHORA HAHAHAHAHA

# Notas sobre Ternary operator :
# True Value if expression else False Value

x = 5
color = 'red' if x>5 else 'blue'
print(f"The color is {'red' if x==5 else 'blue'}\n")

test_list = ['vermelho' if x == 5 else 'azul', 'verde', 'amarelo']; print(test_list)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#            Esse tipo de operação vai em
#			 QUALQUER LUGAR do Python











