

from art import logo

print(logo)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bid:
            highest_bid = bidding_record[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

record = {}
should_continue = True
print("Welcome to the secret auction program.")
while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    record[name] = bid
    inp = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if inp == "yes":
        print('\n' * 200)
        pass
    else:
        should_continue = False
        find_highest_bidder(record)



