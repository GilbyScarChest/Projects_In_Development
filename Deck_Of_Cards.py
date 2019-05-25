
#### Virtual Deck Of Cards ####
#### By Tyler Gilbert

import random
import pandas as pd
import time


#original deck of cards
deck = ["AH", "KH", "QH", "JH", "10H", "9H", "8H", "7H", "6H", "5H", "4H", "3H", "2H",
        "AC", "KC", "QC", "JC", "10C", "9C", "8C", "7C", "6C", "5C", "4C", "3C", "2C",
        "AD", "KD", "QD", "JD", "10D", "9D", "8D", "7D", "6D", "5D", "4D", "3D", "2D",
        "AS", "KS", "QS", "JS", "10S", "9S", "8S", "7S", "6S", "5S", "4S", "3S", "2S"]

#start with empty discard pile
discard_pile = []

#start with empty hand
hand = []


def Deal_Cards(nCards):
    Deal_Cards.has_been_called = True    # Establishing Deal_Cards has been called ** May need this later for teaching games
    global discard_pile                  # Access discard_pile
    global hand                          # Access hand
    hand = []                            # make sure hand is empty
    for i in range(nCards):
        try:
            randChoice = random.choice(deck)   # pick number(specified by nCards) of random cards from deck
            hand.append(randChoice)            # put those cards into hand
            deck.remove(randChoice)            # remove them from deck
        except:
            Reshuffle()                        # If there aren't enough cards left in deck, call Reshuffle fuction
            break
    for card in hand:                          # Otherwise, move whatever was in hand into discard_pile
        discard_pile.append(card)
    if len(hand) < nCards:
        print('Ready!')
    else:                                      
        print(hand)                     
    
    
    
    
def Reshuffle():
    Reshuffle.has_been_called = True           # Establishing Reshuffle has been called ** May need this later for teaching games
    print("Deck Empty. Reshuffling...")
    time.sleep(2)
    global deck    # Access cards
    deck = ["AH", "KH", "QH", "JH", "10H", "9H", "8H", "7H", "6H", "5H", "4H", "3H", "2H",    # Restore deck to original state
            "AC", "KC", "QC", "JC", "10C", "9C", "8C", "7C", "6C", "5C", "4C", "3C", "2C",
            "AD", "KD", "QD", "JD", "10D", "9D", "8D", "7D", "6D", "5D", "4D", "3D", "2D",
            "AS", "KS", "QS", "JS", "10S", "9S", "8S", "7S", "6S", "5S", "4S", "3S", "2S"]
    global discard_pile    # Access discard_pile
    discard_pile = []     # Empty discard_pile
    global hand          # Access hand
    hand = []           # Empty hand
    

    


#### Current Goals ####
# - Swappable Card Decks which are customizable
# - Teach the app a few standard card games: [Poker, Gin, Golf, War, Blackjack]