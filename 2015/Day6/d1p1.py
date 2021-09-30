import re

def main():
    f = open("inputs.txt","r")
    data = [[0 for x in range(1000)] for y in range(1000)]
    for x in f:
        a = x.split()
        if (x[1] == 'o'):
            for y in range(int(a[1].split(',')[0]),int(a[3].split(',')[0])+1):
                for z in range(int(a[1].split(',')[1]),int(a[3].split(',')[1])+1):
                    data[y][z] += 2 
        if (x[6] == 'n'):
            for y in range(int(a[2].split(',')[0]),int(a[4].split(',')[0])+1):
                for z in range(int(a[2].split(',')[1]),int(a[4].split(',')[1])+1):
                    data[y][z] += 1
        if (x[6] == 'f'):
            for y in range(int(a[2].split(',')[0]),int(a[4].split(',')[0])+1):
                for z in range(int(a[2].split(',')[1]),int(a[4].split(',')[1])+1):
                    if(data[y][z] > 0):
                        data[y][z] -= 1
    count = 0
    for x in range(1000):
        for y in range(1000):
            count += data[x][y]
    f.close()
    print(count)
            

if __name__ == "__main__":
    main()
