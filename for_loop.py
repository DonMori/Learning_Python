# print every element of the list and his respective double

# nums_list = [1,2,3,4,5,6.5,7.5]
# nums_dict = {1: 'One', 2: 'Two'}
# nums_string = 'This is a String'
# nums = 3

# for i in nums_dict.items():
# 	print(i)

# for i in nums_dict.values():
# 	print(i)

# for i in nums_string:
# 	print(i)

# for i in range(nums):
# 	print(i)

# print(range(nums))

practice_list = [[10,40,20,50], [2,42,10], [101,10,4]]

for i in practice_list:
	for j in i:
		if j > 100:
			break
		if j < 50 and j > 9:
			print(j, end = ' ')

