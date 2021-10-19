import re
from functools import reduce

def main():
    f = open('inputs.txt', 'r')
    data = []
    for x in f:
        data = re.findall(r'-?\d+', x)
    total = reduce(lambda x, y: int(x)+int(y), data)  
    print(total)


if __name__ == "__main__":
    main()
