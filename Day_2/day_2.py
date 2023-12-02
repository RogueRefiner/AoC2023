FILENAME = "input.txt"

def readInput(FILENAME: str) -> list:
    with open(FILENAME) as f:
        lines = f.readlines()
    return lines

def parseLine(line: list) -> tuple[list, list, list]:
    red = ([int(word[1::].split(" ")[0]) for word in line if "red" in word])
    blue = ([int(word[1::].split(" ")[0]) for word in line if "blue" in word])
    green = ([int(word[1::].split(" ")[0]) for word in line if "green" in word])
    return red, blue, green

def process_line(line: str) -> list:
    return line.strip().replace(":", ';').replace(",", ';').split(";")

def part1() -> int:
    indexes = []
    lines = readInput(FILENAME)
    for line in lines:
        line = process_line(line)
        red, blue, green = parseLine(line)

        invalidRedGames = [item for item in red if item > 12]
        invalidBlueGames = [item for item in blue if item > 14]
        invalidGreenGames = [item for item in green if item > 13]

        if (len(invalidRedGames) == 0 and len(invalidGreenGames) == 0 and len(invalidBlueGames) == 0):
            indexes.append(int(line[0].split(" ")[1]))

    return sum(indexes)

def part2() -> int:
    lines = readInput(FILENAME)
    sum = 0
    
    for line in lines:
        line = process_line(line)
        red, blue, green = parseLine(line)
        sum += max(red) * max(green) * max(blue)
    
    return sum

if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")