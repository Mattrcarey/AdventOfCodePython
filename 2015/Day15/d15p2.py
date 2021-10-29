
def main():
    f = open("inputs.txt","r")
    data = []
    total = 0
    maxValue = 0
    
    for x in f:
        (name, _, cap, _, dur, _, flav, _, text, _, cals) = x.strip().split()
        data.append([int(cap[:-1]), int(dur[:-1]), int(flav[:-1]), int(text[:-1]), int(cals)])
    
    for a in range(100):
        for b in range(100-a):
            for c in range(100-a-b):
                d = 100-a-b-c
                cap = data[0][0]*a+data[1][0]*b+data[2][0]*c+data[3][0]*d
                dur = data[0][1]*a+data[1][1]*b+data[2][1]*c+data[3][1]*d
                flav = data[0][2]*a+data[1][2]*b+data[2][2]*c+data[3][2]*d
                text = data[0][3]*a+data[1][3]*b+data[2][3]*c+data[3][3]*d
                cals = data[0][4]*a+data[1][4]*b+data[2][4]*c+data[3][4]*d
               
                if (cals != 500):
                    score = 0
                    continue

                if (cap <= 0 or dur <= 0 or flav <= 0 or text <=0):
                    score = 0
                    continue
                
                score = cap*dur*flav*text
                if(score > maxValue):
                    maxValue = score

    print(maxValue)
    
    

if __name__ == "__main__":
    main()
