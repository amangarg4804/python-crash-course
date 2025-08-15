# When you slice a string, you extract a subset of the original string—sometimes referred to as indexing a string. 
# Joining strings is the process of linking two or more strings together to create a bigger string.
#Bracket notation, [ ], is used to specify the start of the index, ending index, or both. 
# If you do not include the starting index, then the slice contains everything from the beginning of the string to the ending index. 
# This is the same if you do not include the ending index. 

#Pro tip: Remember that the indexes in Python start with 0, and not 1.


string1 = "Greetings, Earthlings"
print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”
#Note: When you specify an ending index, Python slices everything up to, but not including the ending index. 
# Notice in the second example the ending index is 8, but the characters sliced are 4–7.

# If your index is negative, Python counts back from the end of the string instead of the beginning.

# Prints “Earthlings” again
print(string1[-10:])

# If your index is beyond the end of the string, Python returns an empty string.

# Prints “” 
print(string1[55:])



#You can also use the join() method, which is very useful when you want to concatenate elements from a list of strings with a specific delimiter. 
# In the following example, we have a list of strings called greetings and we join them with a space using .join(greetings). 
# The join() method concatenates all the strings in the list greetings, and places a space between each string.



greetings = ["Hello", "world"]
print(" ".join(greetings))  # Prints "Hello world"

# You can also concatenate a combination of strings and variables like in the following example.
name = "Alice"
print("Hello, " + name + "!")  # Prints "Hello, Alice!"

# This slices the first three numbers from the string:
phonenum = '2025551212'

# The first 3 digits are the area code:
area_code = "(" + phonenum[:3] + ")"

# This slices the numbers 4–6 from the string.
# The next 3 digits are called the “exchange”:
exchange = phonenum[3:6]

# The last 4 digits are the line number:
line = phonenum[-4:]

def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line

format_phone('2025551212')