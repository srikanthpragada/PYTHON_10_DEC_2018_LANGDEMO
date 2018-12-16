def add(a, b):
    return a + b


def add(a, b, c):
    return a + b + c


def sub(a, b):
    return a - b


def task(a, b, op):
    print(op(a, b))


task(10, 20, add)
task(10, 20, sub)
