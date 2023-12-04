def readInput(FILENAME):
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines