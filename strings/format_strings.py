name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))


name = "Manny"
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

# {:>6.2f} - How does it work? 
# > means right align (just like in ms word etc.)
# 6 means total field width 
# .2f means floating point with 2 decimal places
# so the field has total 6 length and the text will always be right aligned



item = "Purple Cup"
amount = 5
price = amount * 3.25
print(f'Item: {item} - Amount: {amount} - Price: {price:.2f}')


def nametag(first_name, last_name):
    return("{} {}.".format(first_name, last_name[0]))


print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 