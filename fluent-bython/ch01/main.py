from franchDeck import FranchDeck, Card


beer_card = Card(7, "Diamond")
print(beer_card)

deck = FranchDeck()
print(len(deck))

print(deck[0])
print(deck[1])
print(deck[-1])

# print([x for x in deck])

from random import choice

print("==========")
print(choice(deck))
print(choice(deck))
print(choice(deck))

print("==========")
print([x for x in deck[:2]])
print([x for x in deck[12::13]])
print("==========")
for card in deck:
    print(card)
print("==========")
for card in reversed(deck):
    print(card)
print("==========")
print(Card("2", "spades") in deck)
print(Card("2", "beats") in deck)
print("==========")
