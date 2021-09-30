import sys


singc = '+-*/'

def string_parse(input_string):
    """Returns a list of elements of a string that has been broken down into numbers and mathematical operands"""

    array = []
    number = ''
    if len(input_string) and input_string[0] not in singc:
        input_string = '+' + input_string
    for i in input_string:
        if i in singc:
            array.append(number)
            array.append(i)
            number = ''
        else:
            number += i
    array.append(number)
    array = list(filter(lambda x: x, array))
    return array


def calculate(parsed_string, index = 0):
    """Calculates a mathematical expression if it is correct and returns a tuple of the form (True / False, The result value / None)"""

    if index >= len(parsed_string):
        return True, eval(''.join(parsed_string))
    else:
        if parsed_string[index] in singc:
            if index + 1 != len(parsed_string) and parsed_string[index + 1] and parsed_string[index + 1].isdigit():
                return calculate(parsed_string, index + 2)
            else:
                return False, None

       
parsed_string = string_parse(''.join(sys.argv[1:]))
print(calculate(parsed_string)) if parsed_string else print((False, None))