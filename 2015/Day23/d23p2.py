import os
import sys

a = 1
b = 0
i = 0


def main():
    f = open(os.path.join(sys.path[0], "inputs.txt"), "r")
    lines = f.readlines()
    f.close()
    global i
    while i < len(lines):
        execute(lines[i].strip())
    print(b)


def execute(command):
    cmd = command.split(" ")
    if cmd[0] == "jie" or cmd[0] == "jio":
        commandSwitch[cmd[0]](cmd[1][0], cmd[2])
    else:
        commandSwitch[cmd[0]](cmd[1])


def half(register):
    global a, b, i
    i += 1
    if register == "a":
        a = int(a / 2)
    else:
        b = int(b / 2)


def triple(register):
    global a, b, i
    i += 1
    if register == "a":
        a = int(a * 3)
    else:
        b = int(b * 3)


def increment(register):
    global a, b, i
    i += 1
    if register == "a":
        a += 1
    else:
        b += 1


def jump(direction):
    global i
    i = i + int(direction)


def jumpEven(register, direction):
    global a, b, i
    if register == "a" and a % 2 == 0:
        jump(int(direction))
    elif register == "b" and b % 2 == 0:
        jump(int(direction))
    else:
        i += 1


def jumpOne(register, direction):
    global a, b, i
    if register == "a" and a == 1:
        jump(int(direction))
    elif register == "b" and b == 1:
        jump(int(direction))
    else:
        i += 1


commandSwitch = {
    "hlf": half,
    "tpl": triple,
    "inc": increment,
    "jmp": jump,
    "jie": jumpEven,
    "jio": jumpOne,
}

if __name__ == "__main__":
    main()
