greeting = 'Hello'
for char in greeting:
	print(char)

print('---------------------')

for i in range(len(greeting)):
	print(i)

#This while loop is the more “common” while loop that programmers often use. 
# This type of loop involves an index variable to represent the current position within the sequence. 
# Most of the time, this will start with 0 for the initial iteration. Let’s take a look at an example:
print('---------------------')
greeting = 'Hello'
index = 0
while index < len(greeting):
	print(greeting[index])
	index += 1        
	
 #while loop with slicing
print('while loop with slicing')
greeting = 'Hello'
index = 0
while index < len(greeting):
  print(greeting[index:index+1])
  index += 1
#This while loop continues to run as long as the index variable is less than the length of the string, which is determined by using len(greeting). 
# With each iteration, a substring of length 1 is extracted using (greeting[index:index+1]) and printed. 
# Then, the index is incremented by 1 (index += 1) to move to the next position.

  
