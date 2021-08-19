from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

#Creating an empty dictionary
auction = {}

other_bidders = False
while other_bidders is False:
  name = input("What is Your name? \n")
  bid = int(input("What's Your Bid? $"))
  auction[name] = bid 
  bidders = input("Are there any other bidders? Type 'yes' or 'no'").lower()
  if bidders == "no":
    other_bidders = True
  else:
    clear()
  #To check the highest bid
  highest_bid = 0
  for key in auction:
    bid_amount = auction[key]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = key
print(f"The winner is {winner} with a bid of {highest_bid}")
