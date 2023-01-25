# Complete the code in this function.

def balanced_parens(line):
    parens_stack = []
    paren_string = []
    balanced = True
    for i in line:

        if i == "(":
            parens_stack.append(i)
            paren_string.append(i)
        if i == ")":
            paren_string.append(i)
            if balanced and len(parens_stack) == 0:
                balanced = False
            elif balanced and parens_stack.pop() != "(":
                balanced = False

    result = "Y" if balanced else "N"
    output = "".join(paren_string)
    return f"{result} {output}"


# Accept input from standard input
line = "((1+2)*(3+4))"
print(balanced_parens(line))
