import sys 
import os
sys.path.append(os.path.abspath("../"))

FILENAME = ["input.txt", "testInput.txt"]

def checkNumber(i: int, j: list, number: str, matrix: list[list[str]], height: int) -> int: 
    isPart = False
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    if len(j) > 2:
        j = [j[0], j[-1]]

    for jj in range(0, len(j)): # consider first and last index of the number
        for dx, dy in directions:   # check all surrounding indices
            ni = i + dx
            nj = j[jj] + dy
            if 0 <= ni < height and 0 <= nj < height: 
                if matrix[ni][nj] != "." and matrix[ni][nj].isdigit() == False:
                    isPart = True
                    break
    if isPart == True:
        return int(number)
    else: 
        return 0

def part1() -> int: 
    sum = 0
    with open(FILENAME[0], 'r') as f:
        lines = f.readlines()
        matrix = [] 
        for line in lines:
            new = [line.strip("\n")]
            matrix.append(new[0])

        height = len(matrix) # = width

    for i in range(0, len(matrix)):
        number = ""
        index = []
        j = 0
        while j < len(matrix[i]):
            if matrix[i][j].isdigit():
                number += matrix[i][j]
                index.append(j)
                if j == len(matrix[i]) - 1: # If Number ends on the last index
                    sum += checkNumber(i, index, number, matrix, height)                
            elif number != "":
                sum += checkNumber(i, index, number, matrix, height)
                number = ""
                index = []
            j += 1    

    return sum

def part2():
    #TODO: 
    pass

if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")