for x in range(5): # range starts with 0 and till <5
    print(x)

print("next program")
for n in range(1,10): # range starts with 1 and till <10. 
  print(n)   
 

friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)

values = [ 23, 52, 59, 37, 48 ]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print("Total sum: " + str(sum) + " - Average: " + str(sum/length))

def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10): # this is similar to starting with x = 0; x< 101 ; x = x+10
  print(x, to_celsius(x))


input = "Four score and seven years ago"  

print([c for c in input if c.lower() in ['a', 'e', 'i', 'o', 'u']])