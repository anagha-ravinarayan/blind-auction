from replit import clear
from art import logo

bids = {}
response = "yes"

print(logo)
print("Welcome to this blind auction. Place your bids! \n")
while response == "yes":
  name = input("What's your name?: ")
  bid_value = int(input("What's your bid?: $"))
  bids[name] = bid_value
  response = input("\nDo you want to enter the bid for another user? Type 'yes' or 'no': ").lower()
  if response == "no":
    highest_value = 0
    highest_bidder = ""
    for bidder in bids:
      value = bids[bidder]
      if value > highest_value:
        highest_value = value
        highest_bidder = bidder
    print(f"{highest_bidder} won the auction with a bid of ${highest_value}!")
  elif response == "yes":
    clear()