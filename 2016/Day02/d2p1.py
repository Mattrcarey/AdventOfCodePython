import os
import sys


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
current = [1, 1]


def main():
    global grid, current
    f = open(os.path.join(sys.path[0], "inputs.txt"), "r")
    lines = f.readlines()
    f.close()

    code = ""

    for line in lines:
        instructions = [*line]
        for i in instructions:
            crackCode(i)
        code += str(grid[current[0]][current[1]])

    print(code)


def crackCode(instruction):
    global grid, current
    match instruction:
        case "U":
            if current[0] != 0:
                current[0] -= 1
        case "D":
            if current[0] != 2:
                current[0] += 1
        case "L":
            if current[1] != 0:
                current[1] -= 1
        case "R":
            if current[1] != 2:
                current[1] += 1


if __name__ == "__main__":
    main()
