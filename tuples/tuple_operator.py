# Convert a list to a tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)

print(my_tuple)  # Outputs: (1, 2, 3, 4)

# Remember that although parentheses are often used to define a tuple, 
# they're not always necessary. The following syntax is also valid:

my_tuple = 1, 2, 3, 4
print(my_tuple)  # Outputs: (1, 2, 3, 4)



# A tuple with a list as an element
my_tuple = (1, 2, ['a', 'b', 'c'])

# You can't change the tuple itself
# my_tuple[0] = 3  # This would raise a TypeError

# But you can modify the mutable elements within the tuple
my_tuple[2][0] = 'x'  
print(my_tuple)  # Outputs: (1, 2, ['x', 'b', 'c'])