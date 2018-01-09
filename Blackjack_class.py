#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the Blackjack class, which contains the main functions needed to set up the Blackjack game.
@author: Can Akman @ the Laboratory
@version: 20171218v1.0
"""

import random
            
            
class GamePrep():
    
    def __init__(self, cardDeck, cardValues):
        self.cardDeck = cardDeck
        self.cardValues = cardValues
        
    
    def createDeck(self):
        """
        This function creates a set of 52 playing cards.
        Input: None
        Output: Returns a list of 52 playing cards.
        """
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        cards = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", 
                 "Ten", "Jack", "Queen", "King"]
        cardDeck = []
        
        for card in cards:
            for suit in suits:
                aCard = card + " of "+ suit
                cardDeck.append(aCard)
        
        return cardDeck
    
    
    
    def shuffleDeck(self):
        """
        This function shuffles the deck.
        Input: Takes a list of cards.
        Output: Returns a list of shuffled cards.
        """
        
        random.shuffle(self)
        
        return None
    
    
    
    def assignCardValues(self, cardDeck, cardValues):
        """
        TO DO: Complete documentation.
        """
        for card in range(len(cardDeck)):
            if "Ace" in cardDeck[card]:
                cardValues[(cardDeck[card])] = 1
            elif "Two" in cardDeck[card]:
                cardValues[(cardDeck[card])] = 2
            elif "Three" in cardDeck[card]:
                cardValues[(cardDeck[card])] = 3
            elif "Four" in cardDeck[card]:
                cardValues[(cardDeck[card])] = 4
            elif "Five" in cardDeck[card]:
                cardValues[(cardDeck[card])] = 5
            elif "Six" in cardDeck[card]:
                cardValues[(cardDeck[card])] = 6
            elif "Seven" in cardDeck[card]:
                cardValues[(cardDeck[card])] = 7
            elif "Eight" in cardDeck[card]:
                cardValues[(cardDeck[card])] = 8
            elif "Nine" in cardDeck[card]:
                cardValues[(cardDeck[card])] = 9
            elif "Ten" in cardDeck[card]:
                cardValues[(cardDeck[card])] = 10               
            elif "Jack" in cardDeck[card]:
                cardValues[(cardDeck[card])] = 10
            elif "Queen" in cardDeck[card]:
                cardValues[(cardDeck[card])] = 10
            elif "King" in cardDeck[card]:
                cardValues[(cardDeck[card])] = 10
        
        return cardValues
    
    




