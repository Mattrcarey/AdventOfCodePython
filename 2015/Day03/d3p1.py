import os
import sys


def main():
    f = open(os.path.join(sys.path[0], "inputs.txt"), "r")
    data = f.readline()
    f.close()
    x = 0
    y = 0
    houses = 1
    visited = {(0, 0): 1}
    for i in data:
        if i == "^":
            x += 1
        elif i == "v":
            x -= 1
        elif i == ">":
            y += 1
        else:
            y -= 1
        if not ((x, y) in visited):
            houses += 1
            visited[(x, y)] = 1
    print(houses)


if __name__ == "__main__":
    main()
