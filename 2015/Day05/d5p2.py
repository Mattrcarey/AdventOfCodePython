import os
import sys


def main():
    f = open(os.path.join(sys.path[0], "inputs.txt"), "r")
    count = 0
    for x in f:
        doubles = {}
        lastdouble = None
        last = x[0]
        twoAgo = None
        nice1 = False
        nice2 = False
        for i in x[1:]:
            if i == twoAgo:
                nice1 = True
            if (last + i) in doubles.keys():
                nice2 = True
            doubles[lastdouble] = 1
            lastdouble = last + i
            twoAgo = last
            last = i
        if nice1 and nice2:
            count += 1

    print(count)
    f.close()


if __name__ == "__main__":
    main()
