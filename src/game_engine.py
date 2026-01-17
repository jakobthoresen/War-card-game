from deck import Deck
from player import Player


class GameEngine:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player1 = Player("Player1")
        self.player2 = Player("Player2")
        self.table = []


    def setup(self):
         
        player1_count = 0
        player2_count = 0

        while len(self.deck) > 0: # Deals out the whole deck

            if player1_count == player2_count:
              self.player1.add_cards([self.deck.deal()])
              player1_count += 1

            else:
                self.player2.add_cards([self.deck.deal()])
                player2_count += 1


    def resolve_war(self):

        if len(self.player1) == 0 or len(self.player2) == 0: # Checks if both players have enough cards to play the war.
            return
        
        nr_of_war_cards = min(len(self.player1) - 1, len(self.player2) - 1, 3) # Finds the number of burn cards we will use in the war if a player has < 3 cards 
        print(f"Both players burn {nr_of_war_cards}")

        for i in range(nr_of_war_cards):
            self.table.append(self.player1.draw_card())
            self.table.append(self.player2.draw_card())

        player1_war_card = self.player1.draw_card()
        player2_war_card = self.player2.draw_card()

        self.table.extend([player1_war_card, player2_war_card])

        print(f"War decision: {player1_war_card} vs {player2_war_card}")

        if player1_war_card > player2_war_card: # Player 1 wins the war
            print(f"{self.player1.name} won the war and wins {len(self.table)} cards.")
            self.player1.add_cards(self.table)
            self.table = []

        elif player2_war_card > player1_war_card: # Player 2 wins the war
            print(f"{self.player2.name} won the war and wins {len(self.table)} cards.")
            self.player2.add_cards(self.table)
            self.table = []
        
        else:
            print("NEW WAR!") # Recursively calls resolve_war() if the war ends in another war
            self.resolve_war()    


    def is_game_over(self): # Returns True if a player has 0 cards
         return not self.player1.has_cards() or not self.player2.has_cards()

    def play_round(self):
        
        card1 = self.player1.draw_card()
        print(f"Player 1 draws {card1}")
        card2 = self.player2.draw_card()
        print(f"Player 2 draws {card2}")
        self.table = [card1, card2]

        if card1 > card2:
            print("Player 1 won the round")
            self.player1.add_cards(self.table)
            self.table = []

        elif card2 > card1:
            print("Player 2 won the round")
            self.player2.add_cards(self.table)
            self.table = []
        
        else:
            print("WAR!")
            self.resolve_war()
            
            