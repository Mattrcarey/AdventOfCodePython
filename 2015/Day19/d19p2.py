import os
import sys
import re


def main():
    f = open(os.path.join(sys.path[0], "inputs.txt"), "r")
    functions = []
    backwardsConversions = []

    for line in f:
        data = line.strip().split(" ")
        if len(data) == 3:
            [before, _, after] = data
            after = re.findall("[A-Z][^A-Z]*", after)
            functions.append(before)
            backwardsConversions.append(after)
        else:
            moleculeVars = re.findall("[A-Z][^A-Z]*", line.strip())

    f.close()
    constants = initializeContants(moleculeVars, functions)
    matches = initializeMatches(backwardsConversions, functions)
    routes = initializeRoutes(moleculeVars, constants)
    visited = set()
    steps = 0

    while True:
        nextRoutes = []
        for x in routes:
            for y in findSwap(x, matches):
                if "".join(y) in visited:
                    continue
                elif y == ["X"]:
                    steps += 1
                    print(f"{steps}")
                    exit()
                nextRoutes.append(y)
                visited.add("".join(y))
                break
        routes = nextRoutes
        steps += 1


def initializeContants(moleculeVars, functions):
    constants = set()
    constants.update(moleculeVars)
    constants.difference_update(functions)
    return constants


def initializeMatches(backwardsConversions, functions):
    matches = []
    for x in backwardsConversions:
        for y in range(len(x)):
            if x[y] in functions:
                x[y] = "X"
        if x not in matches:
            matches.append(x)
    return sorted(matches, key=lambda x: -len(x))


def initializeRoutes(moleculeVars, constants):
    pattern = []
    for x in range(len(moleculeVars)):
        if moleculeVars[x] in constants:
            pattern.append(moleculeVars[x])
        else:
            pattern.append("X")
    return [pattern]


def findSwap(text, data):
    for match in data:
        for x in range(len(text)):
            if text[x : x + len(match)] == match:
                result = text[:x] + ["X"] + text[x + len(match) :]
                yield result


if __name__ == "__main__":
    main()
