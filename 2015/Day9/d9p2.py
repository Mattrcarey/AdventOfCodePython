from itertools import permutations


def main():
    f = open("inputs.txt", "r")
    places = set()
    distances = {} 
    for x in f:
        (source, _, dest, _, distance) = x.split()
        places.add(source)
        places.add(dest)
        distances.setdefault(source, {})[dest] = int(distance)
        distances.setdefault(dest, {})[source] = int(distance)

    longest = 0
    
    for items in permutations(places):
        pathDistance = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
        longest = max(longest, pathDistance)
    
    print(longest)


if __name__ == "__main__":
    main()
