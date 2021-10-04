import math

def notification(): 
        print('Incorrect data')
        exit(1)

class Rational:
    def __init__(self, numerator = 1, denominator = 2):
        try:
            self.__numerator = self.nsd(numerator, denominator)[0]
            self.__denominator = self.nsd(numerator, denominator)[1]
        except:
            notification()

    def str1(self): 
        return str(self.__numerator) + "/" + str(self.__denominator)

    def str2(self): 
        return self.__numerator / self.__denominator
    
    # the method of finding the greatest common divisor
    def nsd(self, numerator, denominator):
        # use the gcd function from the math library
        n_s_d = math.gcd(numerator, denominator)
        # return the tuple
        return numerator//n_s_d, denominator//n_s_d

rational = Rational(8, -4)
print(rational.str1())
print(rational.str2())

rational = Rational('5', 5)
print(rational.str1())
print(rational.str2())
