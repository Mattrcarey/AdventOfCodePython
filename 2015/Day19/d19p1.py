import os
import sys
import re


def main():
    f = open(os.path.join(sys.path[0], "inputs.txt"), "r")
    medMolecule = ""
    conversions = {}
    newMolecules = set()

    for line in f:
        data = line.strip().split(" ")
        if len(data) == 3:
            [before, _, after] = data
            conversions.setdefault(before, []).append(after)
        else:
            medMolecule = line.strip()

    for key in conversions.keys():
        matches = re.finditer(rf"{key}", medMolecule)
        for match in matches:
            start = match.span()[0]
            end = match.span()[1]
            for value in conversions[key]:
                newMolecules.add(medMolecule[:start] + value + medMolecule[end:])

    f.close()
    print(len(newMolecules))


if __name__ == "__main__":
    main()
