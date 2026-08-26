# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)

bids = {}

def find_highest_bidder(bidding_dictionary):
    """Take the bidding dictionary and find the highest bidder"""
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

auction = True

while auction:

    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    bids[name] = price

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bidders == "no":
        auction = False
        find_highest_bidder(bidding_dictionary=bids)
    else:
        print("\n"*50)

