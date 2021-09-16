def main() :
    f = open("d3i1.txt", "r")
    data = f.readline()
    x = 0
    y = 0
    houses = 1
    visited = {(0,0) : 1}
    for i in data :
        if (i=='^') :
            x+=1
        elif (i=='v') :
            x-=1
        elif (i=='>') :
            y+=1
        else :
            y-=1
        if (not ((x,y) in visited)) :
            houses+=1
            visited[(x,y)] = 1
    print(houses)

if __name__ == "__main__" :
    main()
