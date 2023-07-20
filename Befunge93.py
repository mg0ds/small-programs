import random

# https://en.wikipedia.org/wiki/Befunge

def interpret(code):
    output = ""
    stack = []
    code_array = code.split("\n")
    dy = 0
    dx = 1
    run = True
    quote = False
    i = 0
    j = 0

    while run:
        x = code_array[i][j]
        if x == '"' or quote:
            if not quote:
                quote = True
            elif x == '"' and quote:
                quote = False
            else:
                stack.append(ord(x))
        elif x == ">":
            dy = 0
            dx = 1
        elif x == "<":
            dy = 0
            dx = -1
        elif x == "^":
            dy = -1
            dx = 0
        elif x == "v":
            dy = 1
            dx = 0
        elif x == "+":
            stack.append(int(stack.pop()) + int(stack.pop()))
        elif x == "-":
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b - a)
        elif x == "*":
            stack.append(int(stack.pop()) * int(stack.pop()))
        elif x == "/":
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b // a)
        elif x == "%":
            a = int(stack.pop())
            if a == 0:
                stack.append(a)
            else:
                b = int(stack.pop())
                stack.append(b % a)
        elif x == "!":
            if int(stack.pop()) == 0:
                stack.append(1)
            else:
                stack.append(0)
        elif x == "`":
            a = int(stack.pop())
            b = int(stack.pop())
            if b > a:
                stack.append(1)
            else:
                stack.append(0)
        elif x == "?":
            dir_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            random_dir = random.choice(dir_list)
            dy = random_dir[0]
            dx = random_dir[1]
        elif x == "_":
            a = int(stack.pop())
            if a == 0:
                dy = 0
                dx = 1
            else:
                dy = 0
                dx = -1
        elif x == "|":
            a = int(stack.pop())
            if a == 0:
                dy = 1
                dx = 0
            else:
                dy = -1
                dx = 0
        elif x == ":":
            if len(stack) > 0:
                stack.append(stack[-1])
            else:
                stack.append(0)
        elif x == "\\":
            if len(stack) == 1:
                stack.append(0)
            else:
                stack[-1], stack[-2] = stack[-2], stack[-1]
        elif x == "$":
            stack.pop()
        elif x == ".":
            output += str(stack.pop())
        elif x == ",":
            output += chr(stack.pop())
        elif x == "#":
            i += dy
            j += dx
        elif x == "p":
            y = int(stack.pop())
            x = int(stack.pop())
            v = int(stack.pop())
            code_array[y] = code_array[y][:x] + chr(v) + code_array[y][x + 1:]
        elif x == "g":
            y = int(stack.pop())
            x = int(stack.pop())
            if y not in range(0, len(code_array)) or x not in range(0, len(code_array[y])):
                stack.append(0)
            else:
                stack.append(ord(str(code_array[y][x])))
        elif x == "@":
            run = False
        elif x == " ":
            pass
        elif int(x) in range(0, 10):
            stack.append(int(x))

        i += dy
        j += dx
    return output
