file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
  print(extension)

for ext, amount in file_counts.items():
  print("There are {} files with the .{} extension".format(amount, ext))

print(file_counts.keys())
print(file_counts.values())  


## new line
def car_listing(car_prices):
  result = ""
  # Complete the for loop to iterate through the key and value items 
  # in the dictionary.
  for car, cost in car_prices.items():
    result += "A {} costs {} dollars.\n".format(car, cost) # Use a string method to format the required string. 
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Should print:
# A Kia Soul costs 19000 dollars.
# A Lamborghini Diablo costs 55000 dollars.
# A Ford Fiesta costs 13000 dollars.
# A Toyota Prius costs 24000 dollars.