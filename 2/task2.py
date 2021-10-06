from math import gcd


class Rational:
    def __init__(self, numerator = 1, denominator = 2):
        if not (isinstance(numerator, int) or isinstance(denominator, int)):
            raise TypeError('TypeError')
        if denominator == 0:
            raise Exception('Division by zero')
        self.__numerator = self.nsd(numerator, denominator)[0]
        self.__denominator = self.nsd(numerator, denominator)[1]

    def __add__(self, operand):
        if not isinstance(operand, Rational):
            raise TypeError("Error")
        numerator = self.__numerator * operand.__denominator + self.__denominator * operand.__numerator
        denominator = self.__denominator * operand.__denominator
        return Rational(numerator, denominator)

    def __sub__(self, operand):
        if not isinstance(operand, Rational):
            raise TypeError("Error")
        numerator = self.__numerator * operand.__denominator - self.__denominator * operand.__numerator
        denominator = self.__denominator * operand.__denominator
        return Rational(numerator, denominator)

    def __mul__(self, operand):
        if not isinstance(operand, Rational):
            raise TypeError("Error")
        denominator = self.__denominator * operand.__denominator
        numerator = self.__numerator * operand.__numerator
        return Rational(numerator, denominator)

    def __truediv__(self, operand):
        if not isinstance(operand, Rational):
            raise TypeError("Error")
        denominator = self.__denominator * operand.__numerator
        numerator = self.__numerator * operand.__denominator
        return Rational(numerator, denominator)

    def str1(self): 
        return str(self.__numerator) + "/" + str(self.__denominator)

    def str2(self): 
        return self.__numerator / self.__denominator
    
    # the method of finding the greatest common divisor
    def nsd(self, numerator, denominator):
        # use the gcd function from the math library
        n_s_d = gcd(numerator, denominator)
        # return the tuple
        return numerator//n_s_d, denominator//n_s_d

def main():
    try:
        rational1 = Rational(2, 4)
        print(rational1.str1())
        print(rational1.str2())

        rational2 = Rational(5, 4)
        print(rational2.str1())
        print(rational2.str2())

        print('addition: ', (rational1 + rational2).str1(), ' ', (rational1 + rational2).str2())
        print('subtraction: ', (rational1 - rational2).str1(), ' ', (rational1 - rational2).str2())
        print('multiplication: ', (rational1 * rational2).str1(), ' ', (rational1 * rational2).str2())
        print('division: ', (rational1 / rational2).str1(), ' ', (rational1 / rational2).str2())
        return 'All is good!'
    except:
        return 'Something went wrong!'

print(main())