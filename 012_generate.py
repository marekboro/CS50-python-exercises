import random

# def main():
#     coin = random.choice(["heads","tails"])
#     print(coin)

# from random import choice as rndChoice
suits = ["Clubs", "Hearts", "Diamonds", "Spades"]
cards = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
deck = []
def main():
    # get_coinFlip()
    # get_random_fromIntRange(get_int("Range start?:"),get_int("range end?:"))
    # get_random_fromIntRange(1,10)
    # get_randomCard()
    # printCards(cards)
    build_deck()
    printCards(deck)
    shuffleDeck()
    print()
    printCards(deck)

    # shuffleCards()
    # printCards(cards)
    
def get_random_fromIntRange(start,end):
    print(f"{random.randint(start,end)}")

def get_randomCard():
    
    randomCard = random.choice(cards)
    print(f"Card: {randomCard}")

def build_deck():
    for suit in suits:
        for card in cards:
            card = f"{card} of {suit}"
            deck.append(card)

def shuffleDeck():
    random.shuffle(deck)


def shuffleCards():
    random.shuffle(cards)
    # print(shuffled)
    # cards =shuffled

def printCards(inputCards):
    print(f"cards:{inputCards}")

def get_coinFlip():
    # coin = rndChoice(["heads","tails"])
    coin = random.choice(["heads","tails"])
    print(coin)

def get_int(prompt):
    while(True):
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()