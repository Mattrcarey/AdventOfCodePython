import re

def main():
    f = open("inputs.txt", "r")
    data = {}
    isSue = True
    pets = ['children', 'cats', 'samoyeds', 'pomeranians', 'akitas', 'vizslas',
            'goldfish', 'trees', 'cars', 'perfumes']
    petCount = [3,7,2,3,0,0,5,3,2,1]
    
    for x in f:
        (_, num, x, xCount, y, yCount, z, zCount, _) = re.split('\W+', x)
        data.setdefault(num, {})[x] = int(xCount)
        data.setdefault(num, {})[y] = int(yCount)
        data.setdefault(num, {})[z] = int(zCount)
    
    for x in data.keys():
        isSue = True
        count = 0
        for y in range(10):
            if data[x].setdefault(pets[y], petCount[y]) != petCount[y]:
                count+=1
                isSue = False
                continue
        if isSue :
            print(x)


if __name__ == "__main__":
    main()
