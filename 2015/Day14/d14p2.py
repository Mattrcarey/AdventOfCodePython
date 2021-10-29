
def main() :
    f = open("inputs.txt", "r")
    runTime = 2503
    data = {}
    points = {}
    maxDistance = 0
    maxPoints = 0

    for line in f:
        (name, _, _, speed, _, _, time, _, _, _, _, _, _, rest, _) = line.split()
        cycleTime = int(time)+int(rest)
        cycleDistance = int(time)*int(speed)
        div, mod = divmod(runTime, cycleTime)
        data[name] = (int(speed),int(time),cycleDistance,cycleTime)


    for i in range(1,runTime+1):
        maxReindeer = ""
        maxDistance = 0
        for x in data.keys() :
            (speed,time,cycleDistance,cycleTime) = data[x]
            div, mod = divmod(i, cycleTime)
            distance = div*cycleDistance + min(mod, time)*speed
            if distance > maxDistance:
                maxDistance = distance
                maxReindeer = x
        points[maxReindeer] = points.setdefault(maxReindeer, 0) + 1

    
    for x in points.keys() :
        print(x + ": " + str(points[x]))
        if points[x] > maxPoints:
            maxPoints = points[x]
    
    print(maxPoints)

if __name__ == "__main__" :
    main()
