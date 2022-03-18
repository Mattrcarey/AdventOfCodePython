from xxlimited import new
from numpy import *  

def main():
    f = open("inputs.txt", "r")
    data = []

    emptyRow = ['.'] * 102
    data.append(emptyRow)

    for line in f:
        data.append(['.'] + list(line.strip()) + ['.'])

    data.append(emptyRow)
    turnOnCorners(data)

    for x in range(100):
        data = iterate(data)

    count = 0

    for x in range (102):
        for y in range(102):
            if (data[x][y] == '#'):
                count += 1
    
    print(count)

def iterate(data):
    newData = [['.' for x in range(102)] for y in range(102)]

    for x in range(1,101):
        for y in range(1,101):
            if(getTurnedOn(data, x, y, (data[x][y] == '#'))):
                newData[x][y] = '#'
            else:
                newData[x][y] = '.'
    
    turnOnCorners(newData)
    return newData


def getTurnedOn(data, xPosition, yPosition, isTurnedOn):
    onCount = 0

    for x in range(xPosition-1, xPosition+2):
        for y in range(yPosition-1, yPosition+2):
            if(data[x][y] == '#'):
                onCount += 1

    if (isTurnedOn):
        onCount -= 1
    
    if (isTurnedOn and (onCount == 2 or onCount == 3)):
        return True
    if (not isTurnedOn and onCount == 3):
        return True
    return False

def turnOnCorners(data):
    data[1][1] = "#"
    data[1][100] = "#"
    data[100][1] = "#"
    data[100][100] = "#"


def prettyPrint(data):
    for x in data:
        print(x)

if __name__ == "__main__":
    main()