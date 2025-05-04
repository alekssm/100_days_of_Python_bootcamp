# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

print(art.logo)
print("Welcome to the secret blind auction program")

auctions = {}


while True:
    name = input("What is your name? ")
    bid = float(input("What is your bid? "))

    auctions[name] = bid

    new_bid = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    while new_bid != "yes" and new_bid != "no":
        new_bid = input("Invalid answer: Are there any other bidders? Type 'yes' or 'no' ").lower()

    if new_bid == "yes":
        continue
    else:
        break

highest_bid = 0
highest_bidder = ""
for key, value in auctions.items():
    if value > highest_bid:
        highest_bid = value
        highest_bidder = key

print(f"The winner is {highest_bidder} with a bid of ${highest_bid:.2f}.")


