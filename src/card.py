class Card():

    def __init__(self, value:int, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return(f"{self.value} of {self.suit}")
    
    def __gt__(self, other):
        return self.value > other.value