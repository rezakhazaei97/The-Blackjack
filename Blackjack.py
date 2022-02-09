import os
import random
import sys

import termcolor2
import pyfiglet


def playGame():
    cardList = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    playerCard = [random.choice(cardList), random.choice(cardList)]
    computerCard = [random.choice(cardList), random.choice(cardList)]

    print(f"computer card is: [{computerCard[0]}]")
    print(f"your cards are: {playerCard}")
    if sum(playerCard) == 21:
        print(f"computer cards are: {computerCard}")
        print(f"player cards are: {playerCard}")
        print("you won :)")
        playAgain()
    elif sum(computerCard) == 21:
        print(f"computer cards are: {computerCard}")
        print(f"player cards are: {playerCard}")
        print("you lose :(")
        playAgain()
    playerChoice = input("Hit or stand: ")
    computerChoice = [1, 2]
    while playerChoice == "Hit" or playerChoice == "hit":
        print("card added")
        addCard_player = random.choice(cardList)
        playerCard.append(addCard_player)
        print(f"player cards are: {playerCard}")
        if sum(playerCard) > 21:
            print(f"computer cards are: {computerCard}")
            print(f"player cards are: {playerCard}")
            print("you lose :(")
            playAgain()
        playerChoice = input("Hit or stand: ")
    else:
        while sum(playerCard) < 17:
            addCard_player = random.choice(cardList)
            playerCard.append(addCard_player)

    if random.choice(computerChoice) == 1:
        addCard_computer = random.choice(cardList)
        computerCard.append(addCard_computer)
        if sum(computerChoice) > 21:
            print(f"computer cards are: {computerCard}")
            print(f"player cards are: {playerCard}")
            print("you won :(")
            playAgain()
    else:
        while sum(computerCard) < 17:
            addCard_computer = random.choice(cardList)
            computerCard.append(addCard_computer)

    if sum(playerCard) == 21:
        print(f"computer cards are: {computerCard}")
        print(f"player cards are: {playerCard}")
        print("you won :)")
        playAgain()
    elif sum(computerCard) == 21:
        print(f"computer cards are: {computerCard}")
        print(f"player cards are: {playerCard}")
        print("you lose :(")
        playAgain()
    elif sum(playerCard) > 21 and sum(computerCard) > 21:
        print(f"computer cards are: {computerCard}")
        print(f"player cards are: {playerCard}")
        print("Draw")
        playAgain()
    elif sum(playerCard) > 21:
        print(f"computer cards are: {computerCard}")
        print(f"player cards are: {playerCard}")
        print("you lose :(")
        playAgain()
    elif sum(computerCard) > 21:
        print(f"computer cards are: {computerCard}")
        print(f"player cards are: {playerCard}")
        print("you won :)")
        playAgain()
    elif sum(computerCard) == sum(playerCard):
        print(f"computer cards are: {computerCard}")
        print(f"player cards are: {playerCard}")
        print("Draw")
        playAgain()
    elif (21-sum(playerCard)) < (21-sum(computerCard)):
        print(f"computer cards are: {computerCard}")
        print(f"player cards are: {playerCard}")
        print("you won :)")
        playAgain()
    elif (21-sum(computerCard)) < (21-sum(playerCard)):
        print(f"computer cards are: {computerCard}")
        print(f"player cards are: {playerCard}")
        print("you lose :(")
        playAgain()


def playAgain():
    ch = input("do you want to continue?(y/n) ")
    if ch == 'y':
        os.system('cls')
        art()
        playGame()
    else:
        sys.exit()


def art():
    gameName = pyfiglet.figlet_format("The Blackjack")
    print(termcolor2.colored(gameName, color="red"))


art()
playGame()
