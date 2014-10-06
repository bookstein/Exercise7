"""More flexible REPL prefix calculator.

Allows additional operators, so '+ 1 2 3' returns 6.
"""

def add(nums):
    total = nums[0]
    for n in nums[1:]:
        total = total + n
    return total

def subtract(nums):
    total = nums[0]
    for n in nums[1:]:
        total = total - n
    return total

def multiply(nums):
    total = nums[0]
    for n in nums[1:]:
        total = total * n
    return total

def divide(nums):
    total = nums[0]
    for n in nums[1:]:
        total = total / n
    return total

def power(nums):
    total = nums[0]
    for n in nums[1:]:
        total = total ** n
    return total

def square(num):
    return num * num

def cube(num):
    return num * num * num

def modulus(nums):
    total = nums[0]
    for n in nums[1:]:
        total = total % n
    return total


def convert_list_to_ints(lst):
    ints = []
    for n in lst:
        ints.append(int(n))
    return ints


def main():
    while True:
        statement = raw_input("> ")

        tokens = statement.split()
        op = tokens[0]

        if op == "q" or op == "Q":
            break

        nums = convert_list_to_ints(tokens[1:])

        if op == "+" or op == "add":
            print add(nums)

        elif op == "-" or op == "subtract":
            print subtract(nums)

        elif op == "*" or op == "multiply":
            print multiply(nums)

        elif op == "/" or op == "divide":
            print divide(nums)

        elif op == "**" or op == "power":
            print power(nums)

        elif op == "square":
            if len(nums) != 1:
                print "Too many arguments for square"
            else:
                print square(nums[0])

        elif op == "cube":
            if len(nums) != 1:
                print "Too many arguments for cube"
            else:
                print cube(nums[0])

        elif op == "%" or op == "modulo" or op == "modulus":
            print modulus(nums)

        else:
            print "Incorrect operator"


if __name__ == "__main__":
    main()