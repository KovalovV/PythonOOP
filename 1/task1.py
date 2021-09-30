import sys


def input_check(inputString):
    try:
        return eval(" ".join(inputString))
    except:
        return None

print(input_check(inputString = sys.argv[1:]))
