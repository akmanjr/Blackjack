#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the Blackjack class, which contains the main functions needed to set up the Blackjack game.
@author: Can Akman @ the Laboratory
@version: 20171218v1.0
"""

import random


def blackjackRules():
    print("""
RULES of the BLACKJACK GAME:
              
Blackjack is a card game played between the dealer and the player(s). This version of the game is played between the dealer (computer) and one player. 
          
The objective of the game is to beat the dealer, either by:
    (1) getting 21 points on the first 2 cards, without a dealer blackjack;
    (2) getting a final score higher than the dealer, without exceeding 21;
    (3) letting the dealer bust (dealer hand exceeds 21).
              
If the player and dealer hand have the same total, than this is a "push", meaning nobody wins or loses. In other scenarios, the dealer wins.
          
Initially, the player is dealt with 2 cards. Player can draw additional cards to improve his/her hands. 
        
Once the player complete his/her hand, it is dealer's turn. Dealer must hit until the cards sum up to or more than 17 points. 
    """)
        
        

def createDeck():
    """
    This function creates a set of 52 playing cards.
    Input: None
    Output: Returns a list of 52 playing cards.
    """
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    cards = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", 
             "Ten", "Jack", "Queen", "King"]
    myDeck = []
    
    for card in cards:
        for suit in suits:
            aCard = card + " of "+ suit
            myDeck.append(aCard)
    
    return myDeck



def shuffleDeck(deck):
    """
    This function shuffles the deck.
    Input: Takes a list of cards.
    Output: Returns a list of shuffled cards.
    """
    random.shuffle(deck)
    
    return None



def assignCardValues(deckOfCards):
    """
    TO DO: Complete documentation.
    """
    cardValues = {}
    for card in range(len(deckOfCards)):
        if "Ace" in deckOfCards[card]:
            cardValues[(deckOfCards[card])] = 1
        elif "Two" in deckOfCards[card]:
            cardValues[(deckOfCards[card])] = 2
        elif "Three" in deckOfCards[card]:
            cardValues[(deckOfCards[card])] = 3
        elif "Four" in deckOfCards[card]:
            cardValues[(deckOfCards[card])] = 4
        elif "Five" in deckOfCards[card]:
            cardValues[(deckOfCards[card])] = 5
        elif "Six" in deckOfCards[card]:
            cardValues[(deckOfCards[card])] = 6
        elif "Seven" in deckOfCards[card]:
            cardValues[(deckOfCards[card])] = 7
        elif "Eight" in deckOfCards[card]:
            cardValues[(deckOfCards[card])] = 8
        elif "Nine" in deckOfCards[card]:
            cardValues[(deckOfCards[card])] = 9
        elif "Ten" in deckOfCards[card]:
            cardValues[(deckOfCards[card])] = 10               
        elif "Jack" in deckOfCards[card]:
            cardValues[(deckOfCards[card])] = 10
        elif "Queen" in deckOfCards[card]:
            cardValues[(deckOfCards[card])] = 10
        elif "King" in deckOfCards[card]:
            cardValues[(deckOfCards[card])] = 10
    
    return cardValues



def dealCards(hand, deckOfCards):
    """
    TO DO: Complete documentation
    """
    if len(hand) == 0:
        hand.append(deckOfCards.pop(0)), hand.append(deckOfCards.pop(1))
    else:
        hand.append(deckOfCards.pop(0))



def scorePlayerHand(playerHand = [], cardValues = {}):
    """
    TO DO: Complete documentation.
    """
    playerHandSum = 0     # should point out to a Global variable once defined
    
    for card in range(len(playerHand)):
        playerHandSum += cardValues[playerHand[card]]
    
    return playerHandSum
    
    
def scoreDealerHand(dealerHand = [], cardValues = {}):
    """
    TO DO: Complete documentation.
    """
    dealerHandSum = 0     # should point out to a Global variable once defined
    
    for card in range(len(dealerHand)):
        dealerHandSum += cardValues[dealerHand[card]]

    return dealerHandSum





