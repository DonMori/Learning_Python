my_set = {1,2,3,4}
my_set_test = {2,4, 6}
print(my_set)

#use methods
# my_set.add(5)
# print(my_set)

# my_set.remove(2)
# print(my_set)

# print(len(my_set))

# indexing and slicing does NOT work
# print(my_set)

# print(my_set.pop())
# print(my_set)

# Exercise
print(list(my_set)[0])

my_list_set = list(my_set)
print(my_list_set)

print(my_set.union(my_set_test)) # novo set com itens compartilhados (o que um não tem o novo vai ter)
print(my_set.intersection(my_set_test)) # fala oq um não tem do outro (set2 não tem do set1)

print(my_set_test.difference(my_set)) # fala a diferença que um tem do outro

# | = union
# & = intersection
# - = difference

print(my_set | my_set_test)
print(my_set & my_set_test)
print(my_set - my_set_test)


# Exercise - Checking for duplicate items in a list

exercise_list = [1,234,46,3456,234,234,234,234,6,45,6,213,23,42,5346,456,234,1,235,67,67895,67,345,345]
print(len(exercise_list))
print(len(set(exercise_list)))
# set não pode ter elementos repetidos
# então o que for repetido ele ignora
# então eu printo o original e a versão set
# se a versão original for maior que a versão set
# então existem elementos duplicados