# Deck of Cards: Design the data structures for a generic deck of cards. Explain how you would
# subclass the data structures to implement blackjack.

import sys
from enum import Enum

class Suit(Enum):
    CLUB = 0
    DIAMOND = 1
    HEART = 2
    SPADE = 3    

class Card:
    def __init__(self, face_value, suit):
        self.available = True
        self.face_value = face_value
        self.suit = suit

    def is_available(self):
        return self.available
    
    def mark_available(self):
        self.available = True

    def mark_unavailable(self):
        self.available = False


class Deck(Card):
    def __init__(self):
        super().__init__()
        self.cards = []
        self.dealt_index = 0

    def set_deck_of_cards(self):
        for face_value in range(1, 14):
            for suit in Suit:
                card = Card(face_value, suit.name)
                self.cards.append(card)

    def remaining_cards(self):
        return len(self.cards) - self.dealt_index



class Hand(Card):
    def __init__(self):
        self.cards = []

    def get_score(self):
        score = 0
        for card in self.cards:
            score += card.face_value
        return score

    def add_card(self, card):
        self.cards.append(card)


class BlackJackCard(Card):
    def __init__(self, face_value, suit):
        super().__init__(self, face_value, suit)

    def isAce(self):
        return self.face_value == 1
    
    def isFaceCard(self):
        return self.face_value >= 11 and self.face_value <= 13
    
    def min_value(self):
        if self.isAce:
            return 1
        else:
            return self.face_value
    
    def max_value(self):
        if self.isAce:
            return 11
        else:
            return self.face_value

    def value(self):
        if self.isAce:
            return 1
        elif self.isFaceCard:
            return 10
        else:
            return self.face_value
        

class BlackJackHand(Hand):
    def __init__(self):
        super().__init__()

    def get_score(self):
        scores = self.possible_scores()
        max_under = sys.minsize
        min_over = sys.maxsize
        for score in scores:
            if score > 21 and score < min_over:
                min_over = score
            elif score <= 21 and score > max_under:
                max_under = score
        if max_under == sys.minsize:
            return min_over
        else:
            return max_under


    def possible_scores(self):
        hand = self.cards
        scores = []
        for card in hand:
            score = 0
            face_value = card.face_value
            if(not card.isAce):
                score += face_value
            else:
                scores.append(score + 1) # where Ace = 1
                scores.append(score + 11) # where Ace = 11
        return scores
    
    def is_busted(self):
        return self.score > 21

    def is21(self):
        return self.score == 21

    