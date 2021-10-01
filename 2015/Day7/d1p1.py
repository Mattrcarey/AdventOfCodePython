import operator


def notop(x):
    return x ^ 65535


ops = {	"NOT"	:	notop,
		"OR"	:	operator.or_,
		"AND"	:	operator.and_,
		"RSHIFT":	operator.rshift,
		"LSHIFT":	operator.lshift }

data = {}
# Possible values
# - None
# - An integer
# - (value from ops, wire, wire2)
# - (Value from ops, wire)

def main():
    global data
    f = open("inputs.txt","r")
    for x in f:
        a = x.split()
        if (a[0].isnumeric()) :
            data[a[-1]] = int(a[0])
        if (a[1] == "AND") :
            data[a[-1]] = ["AND", a[0], a[2]]
        if (a[1] == "OR") :
            data[a[-1]] = ["OR", a[0], a[2]]
        if (a[1] == "LSHIFT") :
            data[a[-1]] = ["LSHIFT", a[0], a[2]]
        if (a[1] == "RSHIFT") :
            data[a[-1]] = ["RSHIFT", a[0], a[2]]
        if (a[0] == "NOT") :
            data[a[-1]] = ["NOT", a[1]]
        else :
            data[a[-1]] = a[0]
    
    Done = True
    while(1):
        for key in data:
            if (type(data[key])==int):
                continue
            elif (type(data[key])==str):
                if (data[key].isnumeric()):
                    data[key] = int(data[key])
                elif (type(data[data[key]])==int):
                    data[key] = data[data[key]]
                Done = False
            elif (len(data[key]) == 2):
                operation = data[key][0]
                in1 = data[key][1]
                if (in1.isnumeric()):
                    in1 = int(in1)
                else :
                    in1 = data[in1]
                if (type(in1)==int):
                    data[key] = ops[operation](in1)
                    #print(data[key])
                Done = False
            else :
                operation = data[key][0]
                in1 = data[key][1]
                in2 = data[key][2]
                if (in1.isnumeric()):
                    in1 = int(in1)
                else:
                    in1 = data[in1]
                if (in2.isnumeric()):
                    in2 = int(in2)
                else:
                    in2 = data[in2]
                if ((type(in1) == int) and (type(in2) == int)):
                    data[key] = ops[operation](in1,in2)
                    #print(data[key])
                Done = False
        if (Done):
            #for key in data:
            #    print(key + ": " + str(data[key]))
            print(data['a'])
            return
        Done = True


if __name__ == "__main__":
    main()


