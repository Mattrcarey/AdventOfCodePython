def main():
    f = open("inputs.txt", "r")
    line = f.readline()
    f.close()
    floor = 0
    count = 1
    for x in line:
        if (x == '('):
            floor+=1
        elif (x == ')'):
            floor-=1
        if (floor == -1):
            print(count)
            break
        count+=1


if __name__ == "__main__":
    main()
