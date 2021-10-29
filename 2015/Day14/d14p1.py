
def main() :
    f = open("inputs.txt", "r")
    data = {}
    runTime = 2503
    maxDistance = 0
    for line in f:
        (name, _, _, speed, _, _, time, _, _, _, _, _, _, rest, _) = line.split()
        cycleTime = int(time)+int(rest)
        cycleDistance = int(time)*int(speed)
        div, mod = divmod(runTime, cycleTime)
        data[name] = cycleDistance * div + min(mod,int(time)) * int(speed)

    for x in data.keys() :
        if data[x] > maxDistance:
            maxDistance = data[x]
        print(x + ": " + str(data[x]))

    print(maxDistance)

if __name__ == "__main__" :
    main()
