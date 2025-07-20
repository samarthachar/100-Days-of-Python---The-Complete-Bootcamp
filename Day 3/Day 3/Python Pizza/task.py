print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    bill = 0
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y" and size == "S":
    bill += 2
elif pepperoni == "Y":
    bill += 3
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")

