import math
import os
import sys
import re

# Cost : Damage
weapons = {8: 4, 10: 5, 25: 6, 40: 7, 74: 8}
# Cost : Armor
armors = {13: 1, 31: 2, 53: 3, 75: 4, 102: 5}
# Cost : [Damage, Armor]
rings = {25: [1, 0], 50: [2, 0], 100: [3, 0], 20: [0, 1], 40: [0, 2], 80: [0, 3]}

myHealth = 100


def main():
    f = open(os.path.join(sys.path[0], "inputs.txt"), "r")
    lines = f.readlines()
    f.close()

    data = {}
    lowestWinningCost = sys.maxsize
    bossHealth = int(re.search(r"\d+", lines[0].strip()).group())
    bossDamage = int(re.search(r"\d+", lines[1].strip()).group())
    bossArmor = int(re.search(r"\d+", lines[2].strip()).group())

    for x in weapons.keys():
        data.setdefault(x, set()).add(f"{weapons[x]},0")
        getRingOptions(x, 0, data)
        for y in armors.keys():
            data.setdefault(x + y, set()).add(f"{weapons[x]},{armors[y]}")
            getRingOptions(x, y, data)

    for cost in data.keys():
        if cost > lowestWinningCost:
            continue
        for stats in data[cost]:
            if canIWin(stats, bossHealth, bossDamage, bossArmor):
                lowestWinningCost = cost
                break

    print(lowestWinningCost)


def canIWin(stats, bossHealth, bossDamage, bossArmor):
    (damage, armor) = map(int, re.findall(r"\d+", stats))
    myDamage = getDamage(damage, bossArmor)
    bossDamage = getDamage(bossDamage, armor)
    turnsToKill = int(math.ceil(bossHealth / myDamage))
    if bossDamage * (turnsToKill - 1) >= myHealth:
        return False
    return True


def getDamage(damage, armor):
    damage = damage - armor
    if damage > 0:
        return damage
    return 1


def getRingOptions(weapon, armor, data):
    currentCost = weapon + armor
    currentDamage = weapons[weapon]
    currentArmor = 0
    if armor in armors:
        currentArmor = armors[armor]
    for x in rings.keys():
        loopDamage = currentDamage + rings[x][0]
        loopArmor = currentArmor + rings[x][1]
        loopCost = currentCost + x
        key = f"{loopDamage},{loopArmor}"
        data.setdefault(loopCost, set()).add(key)
        for y in rings.keys():
            if x == y:
                continue
            key = f"{(loopDamage + rings[y][0])},{(loopArmor + rings[y][1])}"
            data.setdefault(loopCost + y, set()).add(key)


if __name__ == "__main__":
    main()
