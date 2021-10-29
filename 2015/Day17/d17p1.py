import itertools

def main():
    f = open("inputs.txt", "r")
    data = []
    count = 0
    
    for line in f:
        data.append(int(line))

    for i in itertools.product([True,False], repeat = len(data)):
        total = 0
        itemCount = 0
        for x in i:
            if x:
                total += data[itemCount]
            itemCount += 1
        if total == 150:
            count+=1 
    print(count)

if __name__ == "__main__":
    main()
