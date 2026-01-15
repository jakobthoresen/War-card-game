from card import Card
import random



class Deck():


    def __init__(self):
        SUITS = ["Hearts", "Diamonds", "Spades", "Clover"]
        self.deck = []

        for i in range(2,15):
            for suit in SUITS:
                self.deck.append(Card(i,suit))

    def __len__(self):
        return len(self.deck)
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if self.deck:
            return self.deck.pop()
        return None




