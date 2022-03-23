import os
import sys
import re

spells = {53: 1, 73: 1, 113: 6, 173: 6, 229: 5}
bossDamage = 0

# State is [bossHealth, myHealth, myMana, activeEffects, manaSpent, armor]
def missile(state):
    state[0] -= 4


def drain(state):
    state[0] -= 2
    state[1] += 2


def shield(state):
    state[5] += 7


def poison(state):
    state[0] -= 3


def recharge(state):
    state[2] += 101


command_switch = {53: missile, 73: drain, 113: shield, 173: poison, 229: recharge}


def main():
    global bossDamage
    f = open(os.path.join(sys.path[0], "inputs.txt"), "r")
    lines = f.readlines()
    f.close()

    bossHealth = int(re.search(r"\d+", lines[0].strip()).group())
    bossDamage = int(re.search(r"\d+", lines[1].strip()).group())

    # state is [bossHealth, myHealth, myMana, activeEffects, manaSpent, armor]
    states = [[bossHealth, 50, 500, {}, 0, 0]]
    visitedStates = set()
    wonMana = sys.maxsize

    while not states == []:
        nextStates = []
        for state in states:
            if hash(state) in visitedStates:
                continue
            visitedStates.add(hash(state))
            for x in takeTurn(
                state[0], state[1], state[2], state[3].copy(), state[4], state[5]
            ):
                if x[4] > wonMana:
                    continue
                if bossDead(x):
                    wonMana = x[4]
                nextState = bossTurn(x[0], x[1], x[2], x[3], x[4], x[5])
                if bossDead(nextState):
                    wonMana = x[4]
                    continue
                if meDead(nextState):
                    continue
                nextStates.append(nextState)
            states = nextStates

    print(wonMana)


def takeTurn(bosshealth, myhealth, mana, activeEffects, manaSpent, armor):
    # start of my turn effects
    returnState = [bosshealth, myhealth, mana, activeEffects, manaSpent, armor]
    for x in list(activeEffects.keys()):
        activeEffects[x] -= 1
        command_switch[x](returnState)
        if activeEffects[x] == 0:
            activeEffects.pop(x)

    if bossDead(returnState):
        return returnState

    # My turn do attack / add to active effects
    for x in command_switch.keys():
        if x in activeEffects:
            continue
        if mana >= x:
            turnEffects = returnState[3].copy()
            turnEffects[x] = spells[x]
            mana = returnState[2] - x
            manaSpent = returnState[4] + x
            yield [
                returnState[0],
                returnState[1],
                mana,
                turnEffects,
                manaSpent,
                0,
            ]


def bossTurn(bosshealth, myhealth, mana, activeEffects, manaSpent, armor):
    returnState = [bosshealth, myhealth, mana, activeEffects, manaSpent, 0]
    for x in list(activeEffects.keys()):
        activeEffects[x] -= 1
        command_switch[x](returnState)
        if activeEffects[x] == 0:
            activeEffects.pop(x)

    dmg = bossDamage - returnState[5]
    if dmg > 0:
        returnState[1] -= dmg
    else:
        returnState[1] -= 1

    return returnState


def bossDead(state):
    if state[0] <= 0:
        return True
    return False


def meDead(state):
    if state[1] <= 0:
        return True
    return False


def hash(state):
    effects = list(state[3])
    effects.sort()
    return (
        str(state[0]) + "," + str(state[1]) + "," + str(state[2]) + "," + str(effects)
    )


if __name__ == "__main__":
    main()
