# message = "A kong string with a silly typo"
# message[2] = "l"
#This will throw an error

message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)


pets="Cats & Dogs"
pets.index("&")
pets.index("C")
pets.index("Dog")
pets.index("s") # will only return the first match although there are two s in string

# pets.index("x") #This will throw an error because substring doesn't exis
# so we first have to check whether a substring exists and then call the index method

pets="Cats & Dogs"
print("Dragons" in pets)
print("Cats" in pets)


def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email

print(replace_domain('abc@abc.com', 'abc.com', 'def.com'))


def replace_ending(sentence, old, new):
    # Check if the old substring is at the end of the sentence 
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the 
        # end with the new string
        i = len(sentence) - len(old)
        new_sentence = sentence[:i] + new
        return new_sentence


    # Return the original sentence if there is no match 
    return sentence
    
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"