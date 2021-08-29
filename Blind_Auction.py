import os
from art import logo
print(logo)

def higgest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The highest bidder is {winner} with a bid of ${highest_bid}")
auction_finished = False
while not auction_finished:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    auction = {}

    auction[name] = bid

    choice = input("Are there any other bidders? ").lower()
    if choice == "yes":
        os.system('cls')
    elif choice == "no":
        auction_finished = True
        higgest_bidder(auction)
