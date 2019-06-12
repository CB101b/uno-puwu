#!/usr/bin/python
# The JSON file backups and standard layouts can be found in the 'backups' folder.

import json
import fn
import time
import random

# read json file
cards = json.load(open('cards.json','r'))
cardsInGame = json.load(open('cardsInGame.json','r'))

# variable declarations
playerList = ['player1', 'player2', 'player3', 'player4']
playerAlias = list()

playerAlias.append(input("Enter player 1's name: "))
playerAlias.append(input("Enter player 2's name: "))
playerAlias.append(input("Enter player 3's name: "))
playerAlias.append(input("Enter player 4's name: "))

for i in range(7):
    for player in playerList:
        distroCardType = random.choice(list(cards.keys()))
        distroCard = random.choice(cards[distroCardType])
        print(distroCard)
        fn.moveCardToGameList(distroCard, player, cardsInGame['stack'])


while 1:
    playRound = 0
    while playRound < 4:
        currentPlayer = playerList[playRound]
        currentPlayerAlias = playerAlias[playRound]

        print("It's "+currentPlayerAlias+"'s turn.",end='\n')
        print("You have: ", cardsInGame[currentPlayer], end='\n')
        def choiceloop():
            choice = input('Choose a card: ')
            if choice == '':
                print("You haven't typed a card name. Please try again.")
                time.sleep(0.5)
                choiceloop()
            else:
                return(choice)
        choice = str(choiceloop())
        fn.moveCardToGameList(choice, currentPlayer, cardsInGame['stack'])
        if playRound == 3:
            playRound = 0
        else:
            playRound += 1
