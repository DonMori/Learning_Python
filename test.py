# nome = 'Mori'
# hobby = 'Estudar e aprender programação'
# print(f"Olá, meu nome é {nome}\ne o meu Hobby é {hobby}!")

''' == Lists == 
my_list = [1, 2, 3, 4.5, 'palavra']
print(my_list)
print(len(my_list))
my_list.reverse() # my_list.clear()
print(my_list)
my_list.append("Appended")
print(my_list)
'''

# Tuples    0  -3       1 -2                   2          -1
my_list = ['Ceapeiro', '4SIT', 'Wishes to work at Red | Ventures']
my_tuple = ("Felipe", "16", "Programmer", my_list)
# print(my_tuple)

''' == Tuplas não podem ser modificadas ==
  Used for working with immutable variables 
my_tuple.reverse()
my_tuple.append()
my_tuple.sort()
''' 

# How to pick elements from a tuple or a list?
# Awnser : Indexing or Slicing
#			   |
#			   V
'''              
print(my_tuple[0]) # Felipe
print(my_list[2]) # [...] Red | Ventures
print(my_tuple[3][0],"\n") # Should print 'Ceapeiro' 

print(my_tuple[-1]) # Should print my_list
print(my_list[-2]) # Should print 4SIT
'''

# Exercise
# Can you print 'Hello :)'?
# 	exercise_list = ['first entry', [123,456,[0,'Hello :)']], 'bye']
# 	print(exercise_list[1][2][1])

#                                  == -- Slicing -- ==

# How do i get the [1,2,3,4] 1st and 2nd element from that list?
# Usando [ start : end ]

#            0  1  2  3  4  5  6  7  8  9  10
my_list_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Print 2 to 4 to me please?
# print(my_list_2[1:4]) # same as = print(my_list_2[1:-1])

''' Slicing retorna uma lista
 var = my_list_2[1::]
 print(var)
'''
# print(my_list_2[1:11:2]) # retorna ímpares
# print(my_list_2[0:11:2],"\n") # retorna pares
# 0 -> começo
# 5 e 6 -> até o último elemento
# 2 -> steps of 2 and 2 | aumenta de 2 em 2

# retornar ímpares e pares na ordem inversa

# print(my_list_2[10::-2]) # retorna pares inverso
# print(my_list_2[9::-2],'\n') # retorna ímpares # retorna ímpares

# PRINTA TUDO
# print(my_list_2[::])

# PRINTA TUDO REVERSED
# print(my_list_2[::-1], '\n')

# Exercise
# - start from 8 and go to 2, pick every second element

#print(my_list_2[8:1:-2]) # print(my_list_2[8::-2]) Would work if i removed 0 from the list

# == -- tuple slicing -- ==

#			    0 1 2 3 4 5 6 7 8 9
# test_tuple = (1,2,3,4,5,6,7,8,9,10)
# print(test_tuple[::-2])

# mesma merda do list slicing

# --- === Unpacking === ---
'''
a,b = [10,5] == a,b = (10,5)
print(a,b)

LISTA É A MESMA MERDA DA TUPLAAAAA
the only thing that changes is tuples are immutable
'''

a, b = (my_list_2[5], my_list_2[10])
#                 |_Funciona tmb|__
#				   5             10

print(a)
print(b)

# Criando tuplas

a_list = (1,2,3)
b_list = 1,2,3

print(a_list)
print(b_list)

e, f, g = 10, 'Hello', 4.5
print(e,f,g)

name, age, working = 'Felipe', 16, False
print(f'{name} is {age} years old, and his working state is : {working}\n')

# ---- ==== Exercise ==== ----

value_1, value_2 = 'test', 10 # or value_1, value_2 = value_2, value_1
print(f'value_1 = {value_1}, value_2 = {value_2}')






































