test_dict = {'A': 123, 'B': 456, 'A': 789, 1: True}
#								  ^ Updates the values
# print(test_dict)
print(test_dict.keys()) # Keys
print(test_dict.values()) # Value
print(test_dict.items()) # Prints Keys and Values

# Converting a dict
print(list(test_dict))

# Indexing doesn't work with Dictionaries
# What you need to do is use a Key instead of a number
# ^ and it returns the value atrelated to the key

print(test_dict['A']) # 789 é o valor que está associado a key 'A'
print(test_dict.get('A')) # get method is better because it doesn't crash your code when it doesn't find a key

# Exercise

Dict = {1: 123, 2:456, 3:789}
Dict.update({'a':'aaa'})

print(Dict)






