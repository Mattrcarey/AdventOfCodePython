import os
import sys

coords = [0, 0]
direction = 0  # 0 = north, 1 = east, 2 = south, 3 = west


def main():
    global coords, direction
    f = open(os.path.join(sys.path[0], "inputs.txt"), "r")
    line = f.readline()
    instructions = line.split(", ")
    f.close()

    for i in instructions:
        takeStep(i)

    print(abs(coords[0]) + abs(coords[1]))


def takeStep(instruction):
    global direction
    turn = instruction[:1]
    distance = int(instruction[1:])
    if turn == "R":
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    move(distance)


def move(distance):
    global coords, direction
    match direction:
        case 0:
            coords[1] += distance
        case 1:
            coords[0] += distance
        case 2:
            coords[1] -= distance
        case 3:
            coords[0] -= distance


if __name__ == "__main__":
    main()
