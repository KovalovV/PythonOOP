import sys
from functools import reduce

inputString = sys.argv[1:]
arrayOfArgs = [int(i) for i in inputString[1:]]

dictionary = {'add': reduce(lambda x, y: x + y, arrayOfArgs),
              'sub': reduce(lambda x, y: x - y, arrayOfArgs),
              'mul': reduce(lambda x, y: x * y, arrayOfArgs),
              'div': reduce(lambda x, y: x / y, arrayOfArgs)}

print(dictionary[inputString[0]])