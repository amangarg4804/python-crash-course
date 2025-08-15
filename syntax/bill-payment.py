# Question 2
# In this scenario, two friends are eating dinner at a restaurant. 
# The bill comes in the amount of 47.28 dollars. The friends decide to split the bill evenly between them, 
# after adding 15% tip for the service. Calculate the tip, the total amount to pay, and each friend's share, 
# then output a message saying "Each person needs to pay: " followed by the resulting number.
bill = 47.28 # Assign "bill" variable with bill amount
tip = bill * 0.15 # Multiply by stated tip rate 
total = bill + tip # Sum the "total" of the "bill" and "tip"
share = total/2 # Divide "total" by number of friends dining
print("Each person needs to pay:" + str(share)) # Enter the required string and "share" 
# Hint: Remember to convert incompatible data types