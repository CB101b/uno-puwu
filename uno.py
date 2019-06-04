#!/usr/bin/python
# The JSON file backups and standard layouts can be found in the 'backups' folder.

import json
import fn

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

while 1:
    playRound = 0
    while playRound < 4:
        currentPlayer = playerList[playRound]
        currentPlayerAlias = playerAlias[playRound]

        print("It's "+currentPlayerAlias+"'s turn.",end='\n')
        print("You have: ", cardsInGame[currentPlayer], end='\n')
        choice = input('Choose a card: ')
        fn.moveCardToGameList(choice, currentPlayer)