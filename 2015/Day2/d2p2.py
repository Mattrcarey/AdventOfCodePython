def main():
    f = open("inputs.txt", "r")
    total = 0
    for x in f:    
        data    = x.split("x") 
        largest = max(max(int(data[0]),int(data[1])), int(data[2]))
        if (largest == int(data[0])) :
            total+=int(data[1]) * 2 + int(data[2]) * 2
        elif (largest == int(data[1])) :
            total+=int(data[0]) * 2 + int(data[2]) * 2
        else :
            total+=int(data[0]) * 2 + int(data[1]) * 2
        total += int(data[0]) * int(data[1]) * int(data[2])
    f.close()
    print(total)

if __name__ == "__main__":
    main()
