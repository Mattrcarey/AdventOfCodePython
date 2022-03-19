import os
import sys


def main():
    f = open(os.path.join(sys.path[0], "inputs.txt"), "r")
    countLit = 0
    count = 0
    for x in f:
        countLit += len(x)
        count += len(x) + 2
        y = 0
        while y < len(x):
            if x[y] == "\\" or x[y] == '"':
                count += 1
            y += 1
    print(count - countLit)
    f.close()


if __name__ == "__main__":
    main()
