# In the file arithmetic.py, these function signatures are required

# add(int, int) -> int
# Returns the sum of the two input integers

# subtract(int, int) -> int
# Returns the second number subtracted from the first

# multiply(int, int) -> int
# Multiplies the two inputs together

# divide(int, int) -> float
# Divides the first input by the second, returning a floating point

# square(int) -> int
# Returns the square of the input

# cube(int) -> int
# Returns the cube of the input

# power(int, int) -> int
# Raises the first integer to the power of the second integer and returns the value.

# mod(int, int) -> int
# Returns the remainder when the first integer is divided by the second integer.

def add(*args):
    """Returns the sum of the two input integers"""
    total = 0
    if args[0] == False:
        return total
    for a in args[0]:
        total = total + float(a)
    return total

def subtract(*args):
    """Returns the second number subtracted from the first"""
    if args[0] == False:
        return 0
    total = args[0][0] #- args[0][1]
    for a in args[0]:
        total = total - float(a)
    return total

def multiply(*args):
    """Multiplies the two inputs together"""
    total = num1 * num2
    if args[0] == False:
        return total
    for a in args[0]:
        total = total * float(a)
    return total

def divide(*args):
    pass
    """Divides the first input by the second, returning a floating point"""
    total = num1 / num2
    if args[0] == False:
        return total
    for a in args[0]:
        total = total / float(a)
    return total

def square(*args):
    pass
    """Returns the square of the input"""
    return num1**2

def cube(*args):
    pass
    """ Returns the cube of the input"""
    return num1**3

def power(*args):
    pass
    """Raises the first integer to the power of the second integer and returns the value"""
    total = num1 ** num2
    if args[0] == False:
        return total
    for a in args[0]:
        total = total ** float(a)
    return total

def mod(*args):
    pass
    """Returns the remainder when the first integer is divided by the second integer."""
    total = num1 % num2
    if args[0] == False:
        return total
    for a in args[0]:
        total = total % float(a)
    return total