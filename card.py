from dataclasses import dataclass
from enum import Enum
import random

class ElementType(Enum):
	FIRE = "Fire"
	WATER = "Water"
	EARTH = "Earth"
	AIR = "Air"

class Debuff(Enum):
	BURNING = "Burning"
	SLIPPERY = "Slippery"
	ROUGHSKIN = "Roughskin"
	CHAPPED = "Chapped"

@dataclass
class Card:
	description: str
	manaCost: int
	elementType: ElementType

def calculateTotalMana(playerHand: list[Card]) -> int:
	mana = 0
	for card in playerHand:
		mana += card.manaCost
	return mana

if __name__ == "__main__":
	from player import Player
	def playerHandOptions(player: Player):
		while True:
			for index, card in enumerate(player.hand, start=1):
				print(f"{index}. Mana cost = {card.manaCost}, element = {card.elementType.value}")
			try:
				choice = int(input("Please enter the number associated with the card you'd like to play: "))
				if player.hand[choice - 1].manaCost > player.mana:
					print("You don't have the mana to play this card.")
					continue
					
				print(f"you have played {player.hand[choice - 1]}")
			except ValueError:
				print("Invalid choice. Please enter a valid number.")
			
			return False
		
		
	player1 = Player(hand=[])
	player2 = Player(hand=[])
	for i in range(10):
		if i % 2:
			player1.hand.append(
				Card(
					f"This was the {i + 1} card in deck",
					random.randint(0, 4),
					random.choice(list(ElementType))
				)
			)
		else:
			player2.hand.append(
				Card(
					f"This was the {i + 1} card in deck",
					random.randint(0, 4),
					random.choice(list(ElementType))
				)
			)
	# print("player 1 cards: ")
		# player1.viewHand()
	# print("player 2 cards: ")
		# player2.viewHand()
	playerHandOptions(player1)
	# print(f"total mana cost of player 2's hand = {calculateTotalMana(player2.hand)}")