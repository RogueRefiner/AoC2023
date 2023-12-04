import sys 
import os
sys.path.append(os.path.abspath("../"))

from helper import readInput
from collections import defaultdict


FILENAME = ["input.txt", "testInput.txt", "testInput2.txt"]

def processInput(lines: list[str]) -> list[str]:
    possibleWinningCards = []
    cardsInSet = []

    for line in lines:
        line = line.split(" | ")
        possibleWinningCards.append(line[0].split(":")[1][1::].split(" "))
        cardsInSet.append(line[1].split(" "))
    return possibleWinningCards, cardsInSet

def removeWhiteSpaces(possibleWinningCards: list[str], cardsInSet: list[str]) -> list[str]:
    possibleWinningCards = [x for x in possibleWinningCards if x]
    cardsInSet = [x for x in cardsInSet if x]
    return possibleWinningCards, cardsInSet

def getWinningCards(possibleWinningCards: list[str], cardsInSet: list[str]) -> set:
    return list(set(possibleWinningCards).intersection(cardsInSet))

def part1() -> int:
    sum = 0
    lines = readInput(FILENAME[0])
    allWinningCards, cardsInSet = processInput(lines)
    
    for i in range(0, len(allWinningCards)):
        allWinningCards[i], cardsInSet[i] = removeWhiteSpaces(allWinningCards[i], cardsInSet[i])
        winningNumbers = getWinningCards(allWinningCards[i], cardsInSet[i])
        if(len(winningNumbers) > 0):
            sum += pow(2, len(winningNumbers) - 1)
    
    return sum

def part2() -> int:
    cards = defaultdict(int)
    sum = 0
    lines = readInput(FILENAME[0])
    allWinningCards, cardsInSet = processInput(lines)
    
    for index in range(1, len(allWinningCards)+1):
        allWinningCards[index-1], cardsInSet[index-1] = removeWhiteSpaces(allWinningCards[index-1], cardsInSet[index-1])
        winningNumbers = getWinningCards(allWinningCards[index-1], cardsInSet[index-1])
        cards[index] += 1 # add the original card

        for numberOfCards in range(0, cards[index]): # iterate through each instance of the a card (original + all copies) 
            for cardNumberToAdd in range(1, len(winningNumbers)+1): # loop through all cards that need to be added
                indexToAddACard = index + cardNumberToAdd # e.g. index: 3, addCardNumber: 1, indexToAddACard: 4. Add a 4 Card
                                                          # e.g. index: 3, addCardNumber: 2, indexToAddACard: 5. Add a 5 Card etc.
                                                          # Add index of current Card to get the next index where a card needs to be added
                cards[indexToAddACard] += 1        

    # iterate through the dict and sum all cards
    for card in range(1, len(cards) + 1):
        sum += cards[card]

    return sum

if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
