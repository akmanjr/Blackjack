#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 22:31:45 2017

@author: canakman
"""

import Blackjack

newDeck = Blackjack.createDeck()

def dealCards(hand, deckOfCards):
    """
    TO DO: Complete documentation
    """
    if len(hand) == 0:
        hand.append(deckOfCards.pop(0)), hand.append(deckOfCards.pop(1))
    else:
        hand.append(deckOfCards.pop(0))



def assignCardValues(deckOfCards = []):
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

cardValues = assignCardValues(newDeck)

playerHand = ["Jack of Spades", "Ace of Clubs"]
dealerHand = ["Ace of Diamonds", "Two of Spades"]


def scoreHand(playerHand = [], dealerHand = [], cardValues = {}):
    """
    TO DO: Complete documentation.
    """
    playerHandSum = 0
    dealerHandSum = 0
   
    for card in range(len(playerHand)):
        playerHandSum += cardValues[playerHand[card]]
    
    for card in range(len(dealerHand)):
        dealerHandSum += cardValues[dealerHand[card]]

    print("Player Hand sum is " + str(playerHandSum))
    print("Dealer Hand sum is " + str(dealerHandSum))

scoreHand(playerHand, dealerHand, cardValues)

