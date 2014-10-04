"""
calculator.py

Recreated calculator exercise on my own for practice.
Takes a command and any number of args for math operations.
"""
import arithmetic_mytry

def main():

    arithmetic_functions = {
    '+': arithmetic_mytry.add,
    '-': arithmetic_mytry.subtract,
    '*': arithmetic_mytry.multiply,
    '/': arithmetic_mytry.divide,
    'pow': arithmetic_mytry.power,
    'square': arithmetic_mytry.square,
    'cube': arithmetic_mytry.cube,
    'mod': arithmetic_mytry.mod,
    }

    while True:
        # get user input
        user_input = raw_input("> ")

        # turn user input into a list
        tokens = user_input.split()

        cmd = tokens[0]
        # check if first item is Q or q
        if cmd == "q" or cmd == "Q":
            break

        if cmd in arithmetic_functions:
            # try / except -- check validity of input
            try:
                for idx in range(1, len(tokens)):
                    if tokens[idx] == "0":
                       tokens[idx] = int(tokens[idx])
                    elif float(tokens[idx]):
                        tokens[idx] = float(tokens[idx])
                        #print tokens[idx]

            except:
                print "Please enter valid numbers. Try again"
                continue

            # use dictionary and dispatch method to call function
            print arithmetic_functions[cmd](tokens[1:])

        else:
            print "That was not a valid entry. Please choose a valid mathematical operation from the following list:"
            for key in arithmetic_functions:
                print key


if __name__ == '__main__':
    main()