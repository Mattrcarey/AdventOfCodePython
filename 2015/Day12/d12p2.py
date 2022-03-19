import os
import sys
import re
from functools import reduce
import json


def removeReds(data):
    if isinstance(data, list):
        output = []
        for x in data:
            output.append(removeReds(x))
        return output
    elif isinstance(data, dict):
        output = []
        if "red" not in data.values():
            for k in data.keys():
                output.append(removeReds(data[k]))
            return output
    else:
        return data


def main():
    f = open(os.path.join(sys.path[0], "inputs.txt"), "r")
    jsonData = f.read()
    data = json.loads(jsonData)
    noRedData = str(removeReds(data))
    nums = re.findall(r"-?\d+", noRedData)
    total = reduce(lambda x, y: int(x) + int(y), nums)
    print(total)
    f.close()


if __name__ == "__main__":
    main()
