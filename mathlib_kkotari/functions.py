def add(*args):
    return sum(args)

def mul(*args):
    total = 1
    for num in args:
        total *= num
    return total
