def main():
    f = open("d2i1.txt", "r")
    total = 0
    for x in f:
        data = x.split('x')
        side1 = int(data[0]) * int(data[1])
        side2 = int(data[1]) * int(data[2])
        side3 = int(data[2]) * int(data[0])
        total += 2 * side1 + 2 * side2 + 2 * side3
        total += min(min(side1, side2), side3)
    f.close()
    print(total)
 
if __name__ == "__main__":  
    main()
