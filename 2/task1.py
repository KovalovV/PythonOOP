import re


class Rectangle:
    def __init__(self, length = 1, width = 1):
        if not (isinstance(length, (int, float)) or isinstance(width, (int, float))):
            raise TypeError('Invalid input data type')
        self.__length = length  
        self.__width = width
        self.__area = 1
        self.__perimetr = 1

    def __str__(self):
        return f'area = {self.__area}\nperimetr = {self.__perimetr}'

    def set_width(self, width):
        if not 0 < width < 20:
            raise ValueError('Incorrect data input values')
        if not isinstance(width, (int, float)):
            raise TypeError('Invalid input data type')
        self.__width = width

    def set_length(self, length):
        if not 0 < length < 20:
            raise ValueError('Incorrect data input values')
        if not isinstance(length, (int, float)):
            raise TypeError('Invalid input data type')
        self.__length = length

    def get_width(self): 
        return self.__width       
    
    def get_length(self):        
        return self.__length

    def area(self):
        self.__area = self.__width * self.__length
        return self.__area

    def perimeter(self):
        self.__perimetr = 2 * (self.__width + self.__length)
        return self.__perimetr

def main():
    rectangle = Rectangle()
    rectangle.set_length(5.5)
    rectangle.set_width(2)
    rectangle.area()
    rectangle.perimeter()
    print(rectangle)

main()
