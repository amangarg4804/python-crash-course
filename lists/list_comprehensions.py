# List comprehensions are a concise way to create lists in Python. Let’s look at an example:

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)

#This example starts with a list of numbers. The second line of code defines the type of transformation you want to execute on each element in the original list. 
#In this case, you’re using this line of code to create a new list called squared_numbers 
#and apply x ** 2 to square each element in the numbers list. The result of each squared element is then printed in a new list



#Note: List comprehensions can include conditional statements and nested loops, 
# which allows for additional filtering of elements based on specific called conditions.

z = [x for x in range(0,101) if x % 3 == 0]
print(z)


def odd_numbers(n):
	return [x for x in range(0,n+1) if x%2==1]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []