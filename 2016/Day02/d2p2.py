import os
import sys


grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 2, 3, 4, 0, 0],
    [0, 5, 6, 7, 8, 9, 0],
    [0, 0, "A", "B", "C", 0, 0],
    [0, 0, 0, "D", 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]
current = [3, 1]


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
            if grid[current[0] - 1][current[1]] != 0:
                current[0] -= 1
        case "D":
            if grid[current[0] + 1][current[1]] != 0:
                current[0] += 1
        case "L":
            if grid[current[0]][current[1] - 1] != 0:
                current[1] -= 1
        case "R":
            if grid[current[0]][current[1] + 1] != 0:
                current[1] += 1


if __name__ == "__main__":
    main()
