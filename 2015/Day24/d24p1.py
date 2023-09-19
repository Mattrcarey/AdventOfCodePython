import os
import sys

group_size_limit = 0
best_QE_solution = sys.maxsize


def main():
    global group_size_limit, best_QE_solution
    bank = []
    f = open(os.path.join(sys.path[0], "inputs.txt"), "r")
    total = 0
    for x in f:
        total += int(x)
        bank.append(int(x))
    f.close()

    bank.sort(reverse=True)
    group_size_limit = total / 3
    states = [[0, 1, []]]  # [sum, product, [packages]]

    for x in bank:
        nextStates = []
        for state in states:
            newStatesThisStep = createNextSteps(state, x)
            for newState in newStatesThisStep:
                if evaluateState(newState) == True:
                    nextStates.append(newState)
        states = nextStates.copy()

    print(best_QE_solution)


def createNextSteps(state, newPackage):
    dontAddState = [state[0], state[1], state[2].copy()]
    newList = state[2].copy()
    newList.append(newPackage)
    addValueState = [state[0] + newPackage, state[1] * newPackage, newList]
    return [dontAddState, addValueState]


def evaluateState(state):
    global best_QE_solution, group_size_limit
    if state[0] > group_size_limit:
        return False
    if state[1] > best_QE_solution:
        return False
    if state[0] == group_size_limit:
        if state[1] < best_QE_solution:
            best_QE_solution = state[1]
        return False
    return True


if __name__ == "__main__":
    main()
