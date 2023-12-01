import re

FILENAME = "input.txt"
# FILENAME = "testInput2.txt"


def readInput(FILENAME):
    with open(FILENAME) as f:
        lines = f.readlines()
    return lines


def part1() -> int:
    lines = readInput(FILENAME)
    sum = 0
    pattern = r'(\d)'

    for line in lines:
        numbers = re.findall(pattern, line)
        if len(numbers) > 1:
            sum += int(numbers[0] + numbers[len(numbers) - 1])
        else:
            sum += int(numbers[0] + numbers[0])
    return sum


def transformNumber(number: str) -> str:
    ret = 0
    match(number):
        case "one":
            ret = "1"
        case "two":
            ret = "2"
        case "three":
            ret = "3"
        case "four":
            ret = "4"
        case "five":
            ret = "5"
        case "six":
            ret = "6"
        case "seven":
            ret = "7"
        case "eight":
            ret = "8"
        case "nine":
            ret = "9"
    return ret


def part2() -> int:
    lines = readInput(FILENAME)
    sum = 0
    pattern = r'one|two|three|four|five|six|seven|eight|nine|\d'
    for line in lines:
        line = line.replace("one", "one1one").replace("two", "two2two").replace("three", "three3three").replace("four", "four4four").replace(
            "five", "five5five").replace("six", "six6six").replace("seven", "seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine")
        numbers = re.findall(pattern, line)

        if len(numbers) > 1:
            firstNumber = numbers[0]
            secondNumber = numbers[len(numbers) - 1]

            if (len(firstNumber) > 1):
                firstNumber = transformNumber(firstNumber)

            if (len(secondNumber) > 1):
                secondNumber = transformNumber(secondNumber)

            sum += int(firstNumber + secondNumber)

        else:
            number = numbers[0]
            
            if (len(number) > 1):
                number = transformNumber(number)
            
            sum += int(number + number)
            
    return sum


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
