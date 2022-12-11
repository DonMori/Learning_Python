'''
Strings are very similar to lists and tuples
they are essentially containers
but with different formats
'''

test_string = 'this is a test'  
test_list = [1,2,3,4]

# turning a string into a list / tuple

# print(test_string.split()) # -> usa o " " para fazer separações
# print(test_string.split('t')) - '', his is a '', '' es ''

'''
print(list(test_string))
print(tuple(test_string))
Retorns the list / tuple in a string type
'''

# Turning a list / tuple into a string
# print(' '.join(['one', 'two', 'three\n']))
#        ^      ^- Elementos ou lista
#        |          ^- SÓ PODE TER ELEMENTO STRING
#        |
#   Espaço entre cada elemento

# para colocar uma string de números da pra usar
# print(str(test_list))
# prova real :
# print(type(str(test_list)))

word = 'Very big word yay!'
# print(word[::-1]) # Printing word in reverse
# print(word[::2]) # 2 em 2 | Ignores the space between

# Exercise
# remove all the stuff to only get 1 2 3 4 (remove [] and ,)

# Usando replace
# exercise = str(test_list).replace("[", "").replace("]","").replace(",","")

# usando strip E replace // using replace and strip
# exercise = str(test_list).strip('[').strip(']').replace(',','')
# print(exercise)

# print(word[::-1])

test_dict = {'A': 123, 'B': [1,2,3], 1: True}
# print(test_dict)               - {'A': 123, 'B': [1, 2, 3], 1: True}
# print(test_dict.keys())        - dict_keys(['A', 'B', 1])
# print(len(test_dict))          - 3
# # printa as keys do dicionario
# print(list(test_dict))         - ['A', 'B', 1]
# print(tuple(test_dict))        - ('A', 'B', 1)
# print(str(test_dict))          - {'A': 123, 'B': [1, 2, 3], 1: True}

# indexing with dictionaries

# NÃO FUNCIONAAA

print(test_dict['A']) # key no parametro == tem que ser exatamente igual a key a != A

print(test_dict[1])   # retorna o valor da key
print(test_dict.get('A')) # mesma coisa do test_dic['A']
print(test_dict)

# print(test_dict[1])   # retorna o valor da key           - does crash when it doesn't find the key
# print(test_dict.get('A')) # mesma coisa do test_dic['A'] - doesn't crash when it doesn't find the key

test_dict.update(A=321, C='Dead Body' )
print(test_dict)