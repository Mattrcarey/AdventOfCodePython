

def setop(x,y):
    return x

def notop(x,y):
    return x ^ 65535

def orop(x,y):
    return x | y

def andop(x,y):
    return x & y

def rshiftop(x,y):
    return x >> y

def lshiftop(x,y):
    return x << y


ops = { "ASSN"  :   setop,
        "NOT"   :   notop,
        "OR"    :   orop,
        "AND"   :   andop,
        "RSHIFT":   rshiftop,
        "LSHIFT":   lshiftop }

data = {}
data2 = {}

def main():
    global data, data2
    f = open("inputs.txt","r")
    for x in f:
        a = x.split()
        for i in range(len(a)): # still O(n) time because this loop is const
            if (a[i].isnumeric()):
                a[i] = int(a[i])
        if (len(a)==3):         # command is an assignment
            data[a[-1]] = ["ASSN", a[0], 0]
        elif (len(a)==4):       # command is a NOT
            data[a[-1]] = ["NOT", a[1], 0]
        else:                   # command either or, and, lshift or rshift
            data[a[-1]] = [a[1], a[0], a[2]]
    data2 = data.copy()
    data['b'] = ["ASSN", calculate('a', data2), 0]
    print(calculate('a',data)) 


def calculate(key, mydata):
    if (type(key)==int):
        return key
    elif (type(mydata[key])==int):
        return mydata[key]
    else:
        a  = mydata[key]
        mydata[key] = ops[a[0]](calculate(a[1],mydata),calculate(a[2],mydata))
        return mydata[key]
    

if __name__ == "__main__":
    main()
