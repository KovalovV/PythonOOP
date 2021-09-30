class Rational:
    def __init__(self, numerator = 1, denominator = 2): 
        self.__numerator = numerator  
        self.__denominator = denominator
    
    # Функція знаходження найбільшого спільного дільника
    def nsd(__numerator, __denominator):
        while __numerator * __denominator != 0:
            if __numerator >= __denominator:
                __numerator = __numerator % __denominator
            else:
                __denominator = __denominator % __numerator
        return __numerator + __denominator 
    
    #...

rational = Rational()