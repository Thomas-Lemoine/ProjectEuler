#Problem 54 Poker

def Main():
    wins = 0
    f = open('poker.txt','r')
    Lines = f.readlines()
    for line in Lines:
        cards = line.split()
        (l, r) = (cards[:5], cards[5:])
        #print(l,r)
        if compare(l, r):
            wins += 1
            #print("l wins!")
        #else:
            #print("r wins!")
        f.close()
    print(wins)

def values(hand):
    tempstr = ""
    for card in hand:
        tempstr = tempstr + card[0]
    tempstr = sorted(tempstr)
    for i in range(5):
        if tempstr[i] == 'A':
            tempstr[i] = 14
        if tempstr[i] == 'K':
            tempstr[i] = 13
        if tempstr[i] == 'Q':
            tempstr[i] = 12
        if tempstr[i] == 'J':
            tempstr[i] = 11
        if tempstr[i] == 'T':
            tempstr[i] = 10
            
    for i in range(5):
        tempstr[i] = int(tempstr[i])
    
    return sorted(tempstr)[::-1]

def val_comp(lValue,rValue):
    for i in range(5):
        if lValue[i] != rValue[i]:
            if lValue[i] > rValue[i]:
                return True
            return False

def compare(l,r):
    lValue = values(l)
    rValue = values(r)
    
    #Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.    
    royalflushl = royal_flush(l)
    royalflushr = royal_flush(r)
    if royalflushl:
        return True
    if royalflushr:
        return False
    
    #Straight Flush: All cards are consecutive values of same suit.
    
    if (straight_flush(l) > 0) or (straight_flush(r) > 0):
        if straight_flush(l) == straight_flush(r):
            return val_comp(lValue, rValue)
        else:
            return straight_flush(l) > straight_flush(r)
    
    #Four of a Kind: Four cards of the same value.
    
    if (four_of_a_kind(lValue) > 0) or (four_of_a_kind(rValue) > 0):
        if four_of_a_kind(lValue) == four_of_a_kind(rValue):
            return val_comp(lValue, rValue)
        else:
            return four_of_a_kind(lValue) > four_of_a_kind(rValue)
    
    
    #Full House: Three of a kind and a pair.
    
    if (full_house(lValue) > 0) or (full_house(rValue) > 0):
        if full_house(lValue) == full_house(rValue):
            return val_comp(lValue,rValue)
        else:
            return full_house(lValue) > full_house(rValue)
    
    #Flush: All cards of the same suit.
    
    if (flush(l) or flush(r)):
        if (flush(l) == flush(r)):
            return val_comp(lValue,rValue)
        if flush(l):
            return True
        else:
            return False
        
    #Straight: All cards are consecutive values.
    
    if (straight(lValue) or straight(rValue)):
        if straight(lValue) == straight(rValue):
            return val_comp(lValue, rValue)
        else:
            return straight(lValue)
    
    #Three of a Kind: Three cards of the same value.
    if (three_of_a_kind(lValue) > 0) or (three_of_a_kind(rValue) > 0):
        if three_of_a_kind(lValue) == three_of_a_kind(rValue):
            return val_comp(lValue,rValue)
        else:
            return three_of_a_kind(lValue) > three_of_a_kind(rValue)
    
    #Two Pairs: Two different pairs.
    lList = two_pairs(lValue)
    rList = two_pairs(rValue)
    
    if (lList != []) or (rList != []):
        if rList == []:
            return True
        if lList == []:
            return False
        if max(lList) == max(rList):
            if min(lList) == min(rList):
                return val_comp(lValue,rValue)
            else:
                return min(lList) > min(rList)
        else:
            return max(lList) > max(rList)
    
    #One Pair: Two cards of the same value.
    
    if (one_pair(lValue) > 0) or (one_pair(rValue) > 0):
        if one_pair(lValue) == one_pair(rValue):
            return val_comp(lValue, rValue)
        else:
            return one_pair(lValue) > one_pair(rValue)
    
    
    #High Card: Highest value card.
    
    return val_comp(lValue, rValue)
    


def flush(hand):
    for i in range(1,5):
        if hand[i][1] != hand[i-1][1]:
            return False
    return True

def straight(Value):
    for x in range(2,15):
        if x == Value[0]:
            for i in range(1,5):
                if x-i != Value[i]:
                    return False
    return True

def royal_flush(hand):
    if flush(hand):
        Value = values(hand)
        if straight(Value) and max(Value) == 14:
            return True
    return False

def straight_flush(hand):
    Value = values(hand)
    if flush(hand) and straight(values(hand)):
        return max(Value)
    return 0

def four_of_a_kind(Value):
    for x in range(2):
        total = 0
        for i in range(1,4):
            if Value[x*4] != Value[i]:
                break
            if Value[x*4] == Value[i]:
                total += 1
            if total == 3:
                return Value[x*4]
    return 0
    
def full_house(Value):
    if Value[0] == Value[1] == Value[2] and Value[3] == Value[4]:
        return Value[0]
    if Value[2] == Value[3] == Value[4] and Value[0] == Value[1]:
        return Value[2]
    return 0

def three_of_a_kind(Value):
    if len(set(Value)) == 3:
        for i in range(3):
            if Value.count(Value[i]) == 3:
                return Value[i]
    return 0

def two_pairs(Value):
    answer = []
    setVal = set(Value)
    if len(setVal) != 3:
        return []
    for number in setVal:
        if Value.count(number) == 2:
            answer = [number] + answer
    if not three_of_a_kind(Value):
        return answer
    return []

def one_pair(Value):
    setVal = set(Value)
    if len(setVal) != 4:
        return 0
    for number in setVal:
        if Value.count(number) == 2:
            return number
    return 0

Main()