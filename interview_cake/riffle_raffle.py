# Let's write a function to
# tell us if a full deck of cards shuffled_deck
# is a single riffle of two other halves half1 and half2.

# Here's a rigorous definition of the riffle algorithm:
#
# cut the deck into halves half1 and half2
# grab a random number of cards from the top of half1 (could be 0, must be less than or equal to the number of cards left in half1) and throw them into the shuffled_deck
# grab a random number of cards from the top of half2 (could be 0, must be less than or equal to the number of cards left in half2) and throw them into the shuffled_deck
# repeat steps 2-3 until half1 and half2 are empty.

# If shuffled deck is a riffle of half1 and half2- then top card
# in shuffled_deck is either the first card from half1 or half2
def single_raffle(shuffled_deck, half1, half2):
    # If the shuffled deck's length is 0- just return True
    if len(shuffled_deck) == 0:
        return True
    else:
        if shuffled_deck[0] == half1[0]:
            return single_raffle(shuffled_deck[1:], half1[1:], half2)
        elif shuffled_deck[0] == half2[0]:
            return single_raffle(shuffled_deck[1:], half1, half2[1:])
        else:
            return False

shuffled_deck =
half1 =
half2 =
single_raffle()
