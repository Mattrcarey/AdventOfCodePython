import os
import sys
import itertools


def main():
    f = open(os.path.join(sys.path[0], "inputs.txt"), "r")
    data = []
    count = 0

    for line in f:
        data.append(int(line))

    f.close()
    numContainers = len(data)

    for i in itertools.product([True, False], repeat=len(data)):
        total = 0
        itemCount = 0
        cnumContainers = 0
        for x in i:
            if x:
                total += data[itemCount]
                cnumContainers += 1
            itemCount += 1
        if total == 150:
            if cnumContainers < numContainers:
                numContainers = cnumContainers
                count = 1
            elif cnumContainers == numContainers:
                count += 1
    print(count)


if __name__ == "__main__":
    main()
