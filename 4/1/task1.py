from math import gcd


class Rational:
    """
    The Rational class implements the behavior of a rational number. 
    The number is stored in a reduced form.
    """


    def __init__(self, numerator = 1, denominator = 2):
        self.__numerator = self.nsd(numerator, denominator)[0]
        self.__denominator = self.nsd(numerator, denominator)[1]

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, numerator):
        if not isinstance(numerator, int):
            raise TypeError('Must be integer type')

        self.__numerator = numerator

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, denominator):
        if not isinstance(denominator, int):
            raise TypeError('Must be integer type')
        if not denominator:
            raise ValueError('Denominator = 0')

        self.__denominator = denominator

    def __str__(self) -> str:
        return f'{self.numerator}/{self.denominator}'

    # binary operations
    def __add__(self, other):
        """
        Binary operator overload +
        """

            
        if not isinstance(other, (Rational, int)):
            raise TypeError('Invalid input data type')
        return Rational(self.numerator * other.denominator + self.denominator * other.numerator, self.denominator * other.denominator) if isinstance(other, Rational) else Rational(self.numerator + self.denominator * other, self.denominator)

    def __sub__(self, other):
        """
        Binary operator overload -
        """

            
        if not isinstance(other, (Rational, int)):
            raise TypeError('Invalid input data type')
        return Rational(self.numerator * other.denominator - self.denominator * other.numerator, self.denominator * other.denominator) if isinstance(other, Rational) else Rational(self.numerator - self.denominator * other, self.denominator)

    def __mul__(self, other):
        """
        Binary operator overload *
        """

            
        if not isinstance(other, (Rational, int)):
            raise TypeError('Invalid input data type')
        return Rational(self.numerator * other.denominator, self.denominator * other.denominator) if isinstance(other, Rational) else Rational(self.numerator * other, self.denominator)

    def __truediv__(self, other):
        """
        Binary operator overload /
        """

    
        if not isinstance(other, (Rational, int)):
            raise TypeError('Invalid input data type')
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator) if isinstance(other, Rational) else Rational(self.numerator, self.denominator * other)

    # comparison operators
    def __eq__(self, other):
        """
        Comparison operator overload ==
        """


        if not isinstance(other, (Rational, int)):
            raise TypeError('Invalid input data type')
        return self.num() == other.num() if isinstance(other, Rational) else self.num() == other

    def __ne__(self, other):
        """
        Comparison operator overload !=
        """


        if not isinstance(other, (Rational, int)):
            raise TypeError('Invalid input data type')
        return self.num() != other.num() if isinstance(other, Rational) else self.num() != other

    def __gt__(self, other):
        """
        Comparison operator overload >
        """


        if not isinstance(other, (Rational, int)):
            raise TypeError('Invalid input data type')
        return self.num() > other.num() if isinstance(other, Rational) else self.num() > other

    def __ge__(self, other):
        """
        Comparison operator overload >=
        """


        if not isinstance(other, (Rational, int)):
            raise TypeError('Invalid input data type')
        return self.num() >= other.num() if isinstance(other, Rational) else self.num() >= other
    
    def __lt__(self, other):
        """
        Comparison operator overload <
        """


        if not isinstance(other, (Rational, int)):
            raise TypeError('Invalid input data type')
        return self.num() < other.num() if isinstance(other, Rational) else self.num() < other

    def __le__(self, other):
        """
        Comparison operator overload <=
        """


        if not isinstance(other, (Rational, int)):
            raise TypeError('Invalid input data type')
        return self.num() <= other.num() if isinstance(other, Rational) else self.num() <= other

    def num(self): 
        return self.numerator / self.denominator
    
    def nsd(self, numerator, denominator):
        n_s_d = gcd(numerator, denominator)
        return numerator//n_s_d, denominator//n_s_d

def main():
    rational1 = Rational(1, 4)
    print(rational1)

    rational2 = Rational(20, 20)
    print(rational2)

    print('\nwith rational:')

    print(f'addition: {rational1 + rational2} {(rational1 + rational2).num()}')
    print(f'subtraction: {rational1 - rational2} {(rational1 - rational2).num()}')
    print(f'multiplication: {rational1 * rational2} {(rational1 * rational2).num()}')
    print(f'division: {rational1 / rational2} {(rational1 / rational2).num()}')

    print('\nwith integer:')

    print(f'addition: {rational1 + 5} {(rational1 + 5).num()}')
    print(f'subtraction: {rational1 - 5} {(rational1 - 5).num()}')
    print(f'multiplication: {rational1 * 5} {(rational1 * 5).num()}')
    print(f'division: {rational1 / 5} {(rational1 / 5).num()}')

    print('\nwith rational:')

    print(f'{rational1}>{rational2}: {rational1 > rational2}')
    print(f'{rational1}>={rational2}: {rational1 >= rational2}')
    print(f'{rational1}<{rational2}: {rational1 < rational2}')
    print(f'{rational1}<={rational2}: {rational1 <= rational2}')
    print(f'{rational1}=={rational2}: {rational1 == rational2}')
    print(f'{rational1}!={rational2}: {rational1 != rational2}')

    print('\nwith integer:')

    print(f'{rational1}>{5}: {rational1 > 5}')
    print(f'{rational1}>={5}: {rational1 >= 5}')
    print(f'{rational1}<{5}: {rational1 < 5}')
    print(f'{rational1}<={5}: {rational1 <= 5}')
    print(f'{rational1}=={5}: {rational1 == 5}')
    print(f'{rational1}!={5}: {rational1 != 5}')

main()