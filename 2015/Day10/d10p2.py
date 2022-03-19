import sys


def lookSay(n):
    output = []
    current = n[0]
    ccount = 1
    for x in n[1:]:
        if x == current:
            ccount += 1
        else:
            output.append(str(ccount))
            output.append(current)
            current = x
            ccount = 1
    output.append(str(ccount))
    output.append(current)
    return "".join(output)


# This takes input as a command line argument
def main():
    n = sys.argv[1]
    for _ in range(50):
        n = lookSay(n)
    print(len(n))


if __name__ == "__main__":
    main()
