from dataclasses import dataclass
from card import Card, Debuff

@dataclass
class Player:
    hand: list[Card]
    debuffs: list[Debuff]
    mana: int = 1
    health: int = 10
    

    def viewHand(self):
        for card in self.hand:
            print(card)