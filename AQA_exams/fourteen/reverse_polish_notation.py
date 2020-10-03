# loaded from gist: https://gist.github.com/viebel/3d0f146484989b0c5afc29e53e3e9f2c
# This example assumes binary operators, but this is easy to extend.
# Comes from this excellent article: http://blog.reverberate.org/2013/07/ll-and-lr-parsing-demystified.html
ops = {
    "+": (lambda a, b: a + b),
    "-": (lambda a, b: a - b),
    "*": (lambda a, b: a * b),
    "/": (lambda a, b: a / b)
}


def eval(expression):
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token in ops:
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = ops[token](arg1, arg2)
            stack.append(result)
        else:
            stack.append(int(token))

    return stack.pop()


print(eval("12 8 + 4 *"))