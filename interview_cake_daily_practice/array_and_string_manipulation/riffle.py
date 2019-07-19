# riffle-
# cut the deck into two halves- half1 and half2

# grab a random # of cards from the top of half1 (0 less than the
# number of cards left in half 1), throw them in shuffled deck

# grab a random # of cards from the top of half2 (0 less than
# the number of cards left in half 2) throw them into the shuffled deck

# repeat steps 2-3 until half1 and half2 are empty

# function to tell us if a full deck of cards shuffled_deck is a single riffle
# of two other halves half1 and half2

# riffle is a hodge-podge of two halves of a deck

def is_single_riffle(half1, half2, shuffled_deck):
    # Base case
    if len(shuffled_deck) == 0:
        return True

    # If the top of shuffled_deck is the same as the top of half1
    # (making sure first that we have a top card in half1)
    if len(half1) and half1[0] == shuffled_deck[0]:
        # Take the top cards off half1 and shuffled_deck and recurse
        return is_single_riffle(half1[1:], half2, shuffled_deck[1:])

    # If the top of shuffled_deck is the same as the top of half2
    elif len(half2) and half2[0] == shuffled_deck[0]:
        # Take the top cards off half2 and shuffled_deck and recurse
        return is_single_riffle(half1, half2[1:], shuffled_deck[1:])

    # Top of shuffled_deck doesn't match top of half1 or half2
    # so we know it's not a single riffle
    else:
        return False

def is_single_riffle(half1, half2, shuffled_deck,
                 shuffled_deck_index=0, half1_index=0, half2_index=0):
    # Base case we've hit the end of shuffled_deck
    if shuffled_deck_index == len(shuffled_deck):
        return True

    # If we still have cards in half1
    # and the "top" card in half1 is the same
    # as the top card in shuffled_deck
    if ((half1_index < len(half1)) and
            half1[half1_index] == shuffled_deck[shuffled_deck_index]):
        half1_index += 1

    # If we still have cards in half2
    # and the "top" card in half2 is the same
    # as the top card in shuffled_deck
    elif ((half2_index < len(half2)) and
            half2[half2_index] == shuffled_deck[shuffled_deck_index]):
        half2_index += 1

    # If the top card in shuffled_deck doesn't match the top
    # card in half1 or half2, this isn't a single riffle.
    else:
        return False

    # The current card in shuffled_deck has now been "accounted for"
    # so move on to the next one
    shuffled_deck_index += 1
    return is_single_riffle(
        half1, half2, shuffled_deck, shuffled_deck_index,
        half1_index, half2_index)

def is_single_riffle(half1, half2, shuffled_deck):
    half1_index = 0
    half2_index = 0
    half1_max_index = len(half1) - 1
    half2_max_index = len(half2) - 1

    for card in shuffled_deck:
        # If we still have cards in half1
        # and the "top" card in half1 is the same
        # as the top card in shuffled_deck
        if half1_index <= half1_max_index and card == half1[half1_index]:
            half1_index += 1

        # If we still have cards in half2
        # and the "top" card in half2 is the same
        # as the top card in shuffled_deck
        elif half2_index <= half2_max_index and card == half2[half2_index]:
            half2_index += 1

        # If the top card in shuffled_deck doesn't match the top
        # card in half1 or half2, this isn't a single riffle.
        else:
            return False

    # All cards in shuffled_deck have been "accounted for"
    # so this is a single riffle!
    return True
