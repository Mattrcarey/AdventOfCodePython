import os
import sys


def main():
    f = open(os.path.join(sys.path[0], "inputs.txt"), "r")
    line = f.readline()
    f.close()
    count = 0
    for x in line:
        if x == "(":
            count += 1
        elif x == ")":
            count -= 1
    print(count)


if __name__ == "__main__":
    main()
