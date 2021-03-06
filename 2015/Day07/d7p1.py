import os
import sys


def setop(x, y):
    return x


def notop(x, y):
    return x ^ 65535


def orop(x, y):
    return x | y


def andop(x, y):
    return x & y


def rshiftop(x, y):
    return x >> y


def lshiftop(x, y):
    return x << y


ops = {
    "ASSN": setop,
    "NOT": notop,
    "OR": orop,
    "AND": andop,
    "RSHIFT": rshiftop,
    "LSHIFT": lshiftop,
}
data = {}


def main():
    global data
    f = open(os.path.join(sys.path[0], "inputs.txt"), "r")
    for x in f:
        a = x.split()
        for i in range(len(a)):
            if a[i].isnumeric():
                a[i] = int(a[i])
        if len(a) == 3:  # command is an assignment
            data[a[-1]] = ["ASSN", a[0], 0]
        elif len(a) == 4:  # command is a NOT
            data[a[-1]] = ["NOT", a[1], 0]
        else:  # command either or, and, lshift or rshift
            data[a[-1]] = [a[1], a[0], a[2]]
    print(calculate("a"))
    f.close()


def calculate(key):
    global data
    if type(key) == int:
        return key
    elif type(data[key]) == int:
        return data[key]
    else:
        a = data[key]
        data[key] = ops[a[0]](calculate(a[1]), calculate(a[2]))
        return data[key]


if __name__ == "__main__":
    main()
