import os
import sys


def main():
    f = open(os.path.join(sys.path[0], "inputs.txt"), "r")
    data = []
    emptyRow = ["."] * 102
    data.append(emptyRow)

    for line in f:
        data.append(["."] + list(line.strip()) + ["."])

    f.close()
    data.append(emptyRow)

    for x in range(100):
        data = iterate(data)

    count = 0

    for x in range(102):
        for y in range(102):
            if data[x][y] == "#":
                count += 1

    print(count)


def iterate(data):
    newData = [["." for _ in range(102)] for _ in range(102)]

    for x in range(1, 101):
        for y in range(1, 101):
            if getTurnedOn(data, x, y, (data[x][y] == "#")):
                newData[x][y] = "#"
            else:
                newData[x][y] = "."

    return newData


def getTurnedOn(data, xPosition, yPosition, isTurnedOn):
    onCount = 0

    for x in range(xPosition - 1, xPosition + 2):
        for y in range(yPosition - 1, yPosition + 2):
            if data[x][y] == "#":
                onCount += 1

    if isTurnedOn:
        onCount -= 1

    if isTurnedOn and (onCount == 2 or onCount == 3):
        return True
    if not isTurnedOn and onCount == 3:
        return True

    return False


def prettyPrint(data):
    for x in data:
        print(x)


if __name__ == "__main__":
    main()
