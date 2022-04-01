from replit import clear

# HINT: You can call clear() to clear the output in the console.
bids = {}
bid_finished = False


def find_highest_bid(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        biddername = bidder
        bidammount = bidding_record[bidder]
        if bidammount > highest_bid:
            highest_bid = bidammount
            highest_bidder = biddername
    print(f"The highest bidder is {highest_bidder} at ${highest_bid}")


while not bid_finished:
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    bids[name] = bid
    add_people = input("Are they any other bidders? Type 'yes' or 'no': ").lower()
    if add_people == "no":
        bid_finished = True
        find_highest_bid(bids)
    else:
        clear()
