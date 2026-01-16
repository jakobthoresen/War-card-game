class Player():

    def __init__(self, name, cards = None):
        self.name = name
        if cards is None:
            self.cards = []
        else:
            self.cards = cards

    def __len__(self):
        return len(self.cards)

    def has_cards(self):
        return len(self.cards) > 0

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)

    def add_cards(self, cards:list):
        self.cards.extend(cards)
