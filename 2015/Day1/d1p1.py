

def main():
    f = open("d1i1.txt", "r")
    line = f.readline()
    count = 0
    for x in line:
        if (x == '('):
            count+=1
        elif (x== ')'):
            count-=1
    print(count)


if __name__ == "__main__":
    main()
