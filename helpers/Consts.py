digits = [str(i) for i in range(10)]

operations = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y}

global_counter = 0


def is_blank(c):
    return c in [' ', '\t', '\n', '\r']