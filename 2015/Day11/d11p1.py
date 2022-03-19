import re
import sys

# This one takes input as a command line argument
def main():
    p = sys.argv[1]
    valid = False
    while not valid:
        rev = list(p)[::-1]
        i = 0
        for x in rev:  # increment the string
            if x == "z":
                rev[i] = "a"
            else:
                rev[i] = chr(ord(x) + 1)
                break
            i += 1
        p = "".join(rev[::-1])

        increment = False
        for i in range(len(p) - 2):  # check if the string is valid
            if ord(p[i]) == ord(p[i + 1]) - 1 and ord(p[i]) == ord(p[i + 2]) - 2:
                increment = True
                break
        if not increment:  # doesn't have an increment
            continue
        if re.search(r"[iol]", p) != None:  # has an illegal char
            continue
        if len(set(re.findall(r"(.)\1", p))) < 2:  # doesn't have 2 doubles
            continue
        valid = True
    print(p)


if __name__ == "__main__":
    main()
