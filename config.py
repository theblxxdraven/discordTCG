#!/user/bin/env python

VERSION = "0.1"

DECK_SIZE_MINIMUM = 100
STARTING_HAND_SIZE = 7
PACK_PRICE = 100
CHALLENGE_TIMEOUT = 30 #How long to wait for someone to accept a challenge
TURN_TIMEOUT = 300 #How long to wait for someone to do an action on their turn before they forfeit the match
TOKEN = '' #secret

DEFINITIONS = {
	"land": "Your primary resource. must first play these cards labled as land. You use this to pay cards and Node costs. If at 0, you cannot play any card or node costs.",
	"creature": Your cards to attack with and deal lifeforce damage to oppenents. must have land on battlefield eqaul to the cost of the creature to place creature on battlefield.",
	"node": "An object that stays on the board. They can have spawn abilities, death abilities, and abilities that activate on each of your turns.",
	"mill": "Removes the top card of your deck into your hand.",
	"burn": "cards in hand cannot exceed 7. must discard 1 card if cards in hand exceeds 7.",
	"attack": "creature cards can attack opponents to deal lifeforce damage. creature must be out on battlefield for 1 full turn to be used to attack.",
	"lifeforce": Starts at 20, and can go down to 0. If lifeforce hits 0 you lose.",
	"hunger": "Affects how much lifeforce you gain if sacrificing Nodes. You start with 20, and can go down to 0.",
}

#don't touch
matches = {}
