import re
import os
import sys


def main():
    f = open(os.path.join(sys.path[0], "inputs.txt"), "r")
    count = 0
    for x in f:
        a = re.search("[aeiou].*[aeiou].*[aeiou]", x)
        if a:
            b = re.search(r"(\w)\1", x)
            if b:
                c = re.search("ab|cd|pq|xy", x)
                if not c:
                    count += 1
    print(count)
    f.close()


if __name__ == "__main__":
    main()
