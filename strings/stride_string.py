# An optional way to slice an index is by the stride argument, indicated by using a double colon. 
# This allows you to skip over the corresponding number of characters in your index, or if you’re using a negative stride, the string prints backwards.

# In Python, the stride argument is the step size used when slicing sequences (like lists, strings, tuples, ranges).

# The general slice syntax is:
# sequence[start : stop : stride]

# Where:

#start → index to begin from (default: 0)

#stop → index to end before (default: length of sequence)

#stride → how many elements to skip between picks (default: 1)



string1 = "Greetings, Earthlings"

# Prints “Getns atlns”
print(string1[0::2]) # # Every 2nd element

# Prints “sgnilhtraE ,sgniteerG”
print(string1[::-1]) # Negative stride reverses



nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[::2])   # Every 2nd element: [0, 2, 4, 6, 8]
print(nums[1::3])  # Start at index 1, take every 3rd: [1, 4, 7]
print(nums[::-1])  # Negative stride reverses: [9, 8, 7, 6, ... 0]


#Positive stride → moves forward in the sequence.
# Negative stride → moves backward in the sequence.
# Stride > 1 → skips elements.
# Stride = 1 → takes consecutive elements (default).