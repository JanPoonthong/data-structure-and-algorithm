def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


Stack = []
stack_size = 0
postfix_expr = input().split()
for token in postfix_expr:
    if is_number(token):
        Stack.append(int(token))
        stack_size += 1
    else:
        if token == "+":
            Stack[stack_size - 2] = (
                Stack[stack_size - 1] + Stack[stack_size - 2]
            )
            stack_size -= 1
            Stack.pop()
        elif token == "-":
            Stack[stack_size - 2] = Stack[stack_size - 2] - Stack[stack_size - 1]

            stack_size -= 1
            Stack.pop()
        elif token == "*":
            Stack[stack_size - 2] = (
                Stack[stack_size - 2] * Stack[stack_size - 1]
            )
            stack_size -= 1
            Stack.pop()
        elif token == "/":
            Stack[stack_size - 2] = (
                Stack[stack_size - 2] / Stack[stack_size - 1]
            )
            stack_size -= 1
            Stack.pop()
        elif token == "^":
            Stack[stack_size - 2] = (
                Stack[stack_size - 2] ** Stack[stack_size - 1]
            )
            stack_size -= 1
            Stack.pop()
        elif token == "%":
            Stack[stack_size - 2] = (
                Stack[stack_size - 2] % Stack[stack_size - 1]
            )
            stack_size -= 1
            Stack.pop()

print("%.1f" % Stack[0])
