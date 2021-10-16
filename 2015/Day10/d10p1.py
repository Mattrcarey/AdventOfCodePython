import sys


def lookSay(n) :
    output = ""
    current = n[0]
    ccount = 1
    for x in n[1:]:
        if (x == current) :
            ccount+=1
        else:
            output = output + str(ccount) + current
            current = x
            ccount = 1
    output = output + str(ccount) + current
    return output


def main() :
    n = sys.argv[1]
    for x in range(40) :
        n = lookSay(n)
    print(len(n))

if __name__ == "__main__":
    main()
