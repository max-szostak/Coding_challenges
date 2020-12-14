hands_file = open("hands.txt", "r")
hands = hands_file.readlines()

def evaluate(hand):
    ## hand[player][card][value/suit]
    hand = listify(hand)
    return rank(hand[0]) > rank(hand[1])

def listify(hand_string):
    ## hand[player][card][value/suit]
    hand_list_1 = []
    hand_list_2 = []
    for ind in range(0, 28, 3):
        card_list = []
        card_string = hand_string[ind:ind + 2]
        card_list.append(card_string[0])
        card_list.append(card_string[1])
        if ind < 14:
            hand_list_1.append(card_list)
        else:
            hand_list_2.append(card_list)
    hands_list = []
    hands_list.append(hand_list_1)
    hands_list.append(hand_list_2)
    return hands_list

# 0-20 = High Card: Highest value card.
# 21-40 = One Pair: Two cards of the same value.
# 41-60 = Two Pairs: Two different pairs.
# 61-80 = Three of a Kind: Three cards of the same value.
# 81-100 = Straight: All cards are consecutive values.
# 101-120 = Flush: All cards of the same suit.
# 121-140 = Full House: Three of a kind and a pair.
# 141-160 = Four of a Kind: Four cards of the same value.
# 161-180 = Straight Flush: All cards are consecutive values of same suit.
# 181 = Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

## hand[card][value/suit]

def rank(hand):
    suits = [card[1] for card in hand]
    values = convertValues([card[0] for card in hand])
    hand = [[values[i], suits[i]] for i in range(0, len(values))]
    hand.sort(key = getValue)
    values = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    ## check flush
    if len(set(suits)) == 1: 
        if values[0] == 10: 
            return 181 # royal flush
        elif values[4] - values[0] == 4: 
            return 160 + values[4] # straight flush
        if len(set(values)) == 2:
            if values[1] == values[3]: # four of a kind
                return 140 + values[2]
            return 120 + values[2] # full house
        else:
            return 100 + values[4] # flush
    if len(set(values)) == 2:
        if values[1] == values[3]: 
            return 140 + values[2] # four of a kind
        return 120 + values[2] # full house
    if values[4] - values[0] == 4 and len(set(values)) == 5:
        return 80 + values[4] # straight
    if len(set(values)) == 3:
        if values[0] == values[2] or values[1] == values[3] or values[2] == values[4]:
            return 60 + values[2] # three of a kind
        return 40 + values[3] + values[1] * 0.1  + tphc(values) * 0.001 # two pair
    if len(set(values)) == 4: # one pair
        if values[0] == values[1]:
            return 20 + values[0] + ophc(values)
        if values[3] == values[4]:
            return 20 + values[3] + ophc(values)
        return 20 + values[2] + ophc(values)
    return values[4] # high card

def getValue(e):
    return e[0]

def ophc(values):
    # returns the high card combination in a one pair hand
    if values[3] == values[4]:
        return values[2] * 0.1 + values[1] * 0.01 + values[0] * 0.001
    elif values[2] == values[3]:
        return values[4] * 0.1 + values[1] * 0.01 + values[0] * 0.001
    elif values[1] == values[2]:
        return values[4] * 0.1 + values[3] * 0.01 + values[0] * 0.001
    return values[4] * 0.1 + values[3] * 0.01 + values[2] * 0.001

def tphc(values):
    # returns the high card in a two pair hand
    if values[0] == values[1]:
        if values[2] == values[3]:
            return values[4]
        return values[2]
    return values[0]
    
def convertValues(values):
    new_values = []
    for s in values:
        if s == "T":
            new_values.append(10)
        elif s == "J":
            new_values.append(11)
        elif s == "Q":
            new_values.append(12)
        elif s == "K":
            new_values.append(13)
        elif s == "A":
            new_values.append(14)
        else:
            new_values.append(int(s))
    return new_values

counter = 0

for hand in hands:
    if evaluate(hand):
        counter += 1

print(counter)
