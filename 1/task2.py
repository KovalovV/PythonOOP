import sys
import operator


from functools import reduce


def calculate(dictionary):
    try:
        return reduce(dictionary[input_string[0]], array_of_args)
    except:
        return None


def arg_check(input_string):
    singc = '+-/*'
    for i in input_string:
        if i in singc:
            print(None)
            return sys.exit()


input_string = sys.argv[1:]
arg_check(input_string)
array_of_args = [int(i) for i in input_string[1:]]
dictionary = {'add': operator.add,
              'sub': operator.sub,
              'mul': operator.mul,
              'div': operator.truediv}
print(calculate(dictionary))