import random
friends = ["Ross", "Rachel", "Monica", "Joey", "Phoebe", "Chandler"]

print(random.choice(friends))

# or

index = random.randint(0, 5)
print(friends[index])