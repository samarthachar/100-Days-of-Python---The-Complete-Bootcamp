print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tipPercentage = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


tip = bill * (tipPercentage/100)
totalBill = bill + tip
billPerPerson = totalBill / people
finalBill = round(billPerPerson,2)
print(f"Each person should pay: ${finalBill}")