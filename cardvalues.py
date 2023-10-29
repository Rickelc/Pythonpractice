# here I am calculating the total value of a hand for the blackjack simulation
def hand_value(hand):
    total_value = 0
    num_aces = 0
    #determining the values of the cards based on the type of card
    for card in hand:
        #giving the value of 10 for face cards
        if card in ['Jack', 'Queen', 'King']:
            total_value += 10
        #giving the value of aces plus 1 and giving the total value of 11
        elif card == 'Ace':
            num_aces += 1
            total_value += 11
        #adding the integer of the number card for the rest of the deck
        else:
            total_value += int(card)
    #Handling the case in which the value of 11 for the ace would make the player over 21      
    while num_aces > 0 and total_value > 21:
        #subtracting 10 in the case it takes the player over 21
        total_values -= 10
        num_aces -= 1
            
    #returning the total value to the main function        
    return total_value