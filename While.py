run = 0
odd_numbers = []

# Creates a while condition that will run 0-100 and making possible for us to use those numbers on a if statement
while run != 100:
	if run%2 == 1:
		odd_numbers.append(run)
	run+=1

print(odd_numbers)