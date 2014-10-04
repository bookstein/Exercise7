def add(args):
    """Returns the sum of the two input integers"""
    total = 0
    for num in args:
        total += num
    return total

def subtract(args):
    """Returns the second number subtracted from the first"""
    total = args[0]
    for num in args[1:]:
        total -= num
    return total

def multiply(args):
    """Multiplies the two inputs together"""
    total = 1
    for num in args:
        total *= num
    return total

def divide(args):
    total = args[0]
    for num in args[1:]:
        if 0 in args[2:]:
            print "Cannot divide by zero."
            break
        else:
            total = total / num
            return total

def square(args):
    """Returns the square of the input"""
    return args[0]**2

def cube(args):
    """ Returns the cube of the input"""
    return args[0]**3

def power(args):
    """Raises the first integer to the power of the second integer and returns the value"""
    base = args[0]
    for num in args[1:]:
        base = base ** num
    return base

def mod(args):
    """Returns the remainder when the first integer is divided by the second integer."""
    total = args[0]
    for num in args[1:]:
        if 0 in args[2:]:
            print "Cannot divide by zero."
            break
        else:
            total = total % num
            return total