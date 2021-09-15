import sys

singc = '+-*/'

def stringParse(inputString):
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
    if index >= len(parsedString):
        return True, eval(''.join(parsedString))
    else:
        if parsedString[index] in singc:
            if parsedString[index + 1].isdigit():
                return calculate(parsedString, index + 2)
            else:
                return False, None
        

#inputString = ''.join(sys.argv[1:])
parsedString = stringParse(''.join(sys.argv[1:]))
print(calculate(parsedString)) if parsedString else print((False, None))