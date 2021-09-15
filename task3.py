import sys


singc = '+-*/'

def stringParse(inputString):
    """Returns a list of elements of a string that has been broken down into numbers and mathematical operands"""

    array = []
    number = ''
    if len(inputString) and inputString[0] not in singc:
        inputString = '+' + inputString
    for i in inputString:
        if i in singc:
            array.append(number)
            array.append(i)
            number = ''
        else:
            number += i
    array.append(number)
    return list(filter(lambda x: x, array))


def calculate(parsedString, index = 0):
    """Calculates a mathematical expression if it is correct and returns a tuple of the form (True / False, The result value / None)"""

    if index >= len(parsedString):
        return True, eval(''.join(parsedString))
    else:
        if parsedString[index] in singc:
            if parsedString[index + 1].isdigit():
                return calculate(parsedString, index + 2)
            else:
                return False, None

       
parsedString = stringParse(''.join(sys.argv[1:]))
print(calculate(parsedString)) if parsedString else print((False, None))