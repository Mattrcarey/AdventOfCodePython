from itertools import permutations


def main():
    f = open("inputs.txt", "r")
    people = set()
    preferences = {}
    for x in f:
        (person1, _, sign, num, _, _, _, _, _, _, person2) = x.split()
        person2 = person2[:-1]
        people.add(person1)
        people.add(person2)
        if(sign == 'gain'):
            preferences.setdefault(person1, {})[person2] = int(num)
        else:
            preferences.setdefault(person1, {})[person2] = - int(num)
    
    for x in people:
        preferences.setdefault(x, {})['Me'] = 0
        preferences.setdefault('Me', {})[x] = 0
    
    people.add('Me')
    greatest = 0
    for items in permutations(people):
        list1 = list(items)
        list2 = [items[-1]] + list(items[:-1])
        list3 = list(items[1:]) + [items[0]]
        happinessChange = sum(map(lambda x, y, z: preferences[x][y]+preferences[x][z], 
            list1, list2, list3))
        greatest = max(greatest, happinessChange)
    
    print(greatest)


if __name__ == "__main__":
    main()
