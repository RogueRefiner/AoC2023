import sys 
import os
sys.path.append(os.path.abspath("../"))

from helper import readInput

FILENAME = ["input.txt", "testInput.txt", "testInput2.txt"]

def parseLine(line: list) -> tuple[list, list, list]:
    red = ([int(word[1::].split(" ")[0]) for word in line if "red" in word])
    blue = ([int(word[1::].split(" ")[0]) for word in line if "blue" in word])
    green = ([int(word[1::].split(" ")[0]) for word in line if "green" in word])
    return red, blue, green

def processLine(line: str) -> list:
    return line.strip().replace(":", ';').replace(",", ';').split(";")

def part1() -> int:
    indexes = []
    lines = readInput(FILENAME[0])
    for line in lines:
        line = processLine(line)
        red, blue, green = parseLine(line)

        if (max(red) <= 12 and max(blue) <= 14 and max(green) <= 13):
            indexes.append(int(line[0].split(" ")[1]))

    return sum(indexes)

def part2() -> int:
    lines = readInput(FILENAME[0])
    sum = 0
    
    for line in lines:
        line = processLine(line)
        red, blue, green = parseLine(line)
        sum += max(red) * max(green) * max(blue)
    
    return sum

if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")