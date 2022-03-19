import os
import sys


def main():
    f = open(os.path.join(sys.path[0], "inputs.txt"), "r")
    countLit = 0
    count = 0
    for x in f:
        countLit += len(x)
        count += len(x) - 2
        y = 0
        while y < len(x):
            if x[y] == "\\":
                if x[y + 1] == "x":
                    count -= 3
                    y += 3
                else:
                    count -= 1
                    y += 1
            y += 1
    print(countLit - count)
    f.close()


if __name__ == "__main__":
    main()
