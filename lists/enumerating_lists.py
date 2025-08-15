winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
  print("{} - {}".format(index + 1, person))


def skip_elements(elements):
	# code goes here
	result = [];
	for index, element in enumerate(elements): 
		if(index % 2 ==0):
			result.append(element)
	return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']  