def main() :
    f = open("inputs.txt", "r")
    data = f.readline()
    x = 0
    y = 0
    roboX = 0
    roboY = 0
    houses = 1
    visited = {(0,0) : 1}
    count = 0;
    for i in data :
        if (count%2 == 0) :
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
        else :
            if (i=='^') :
                roboX+=1
            elif (i=='v') :
                roboX-=1
            elif (i=='>') :
                roboY+=1
            else :
                roboY-=1
            if (not ((roboX,roboY) in visited)) :
                houses+=1
                visited[(roboX,roboY)] = 1
        count+=1
    print(houses)

if __name__ == "__main__" :
    main()
