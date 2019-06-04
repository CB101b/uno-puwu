import json

# read json file
cards = json.load(open('cards.json','r'))
cardsInGame = json.load(open('cardsInGame.json','r'))

# these will be gone soon
def dumpCards(cardsDictionary):
    with open('cards.json','w') as dump:
        json.dump(cardsDictionary, dump)

def dumpCardsInGame(cardsInGameDictionary):
    with open('cardsInGame.json','w') as dump:
        json.dump(cardsInGameDictionary, dump)

def cardRecognize(cardchoice):
    tempSplit = cardchoice.split('#')[0]
    if tempSplit == 'b':
        return('blue')
    elif tempSplit == 'r':
        return('red')
    elif tempSplit == 'g':
        return('green')
    elif tempSplit == 'y':
        return('yellow')

def moveCardToGameList(cardchoice, currentPlayer):
    tempColor = cardRecognize(cardchoice)
    cards[tempColor].remove(cardchoice)
    cardsInGame[currentPlayer].append(cardchoice)
    dumpCards(cards)
    dumpCardsInGame(cardsInGame)