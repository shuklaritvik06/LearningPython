# Blind Audition

from os import system
print('''
 ____  _ _           _      _             _ _ _   _             
| __ )| (_)_ __   __| |    / \  _   _  __| (_) |_(_) ___  _ __  
|  _ \| | | '_ \ / _` |   / _ \| | | |/ _` | | __| |/ _ \| '_ \ 
| |_) | | | | | | (_| |  / ___ \ |_| | (_| | | |_| | (_) | | | |
|____/|_|_|_| |_|\__,_| /_/   \_\__,_|\__,_|_|\__|_|\___/|_| |_|

''')
bidding = {}
maximum = []
choice = input("Type yes to start: ")
while choice != "no":
    name = input("Enter your name: ")
    bid = int(input("Please enter your bid: $"))
    bidding[name] = bid
    choice = input("\nIs there any other bidder type yes or no: ")
    if choice:
        system('clear')
for key in bidding:
    maximum.append(bidding[key])
maxvalue = max(maximum)
for key in bidding:
    if bidding[key] == maxvalue:
        print("\n\n"+key+" "+"is the highest bidder! SOLD!")
    else:
        pass
print("\nBIDDING CLOSED!! Thanks For Joining!")
