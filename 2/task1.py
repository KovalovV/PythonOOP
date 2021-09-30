class Rectangle:
    def __init__(self, length = 1, width = 1): 
        self.__length = length  
        self.__width = width

    def set_width(self, width):
        try:
            if 0.0 < width < 20.0:
                self.__width = width
                return True
        except:
            return None

    def set_length(self, length):
        try:
            if 0.0 < length < 20.0:
                self.__length = length
                return True
        except:
            return None

    def get_width(self): 
        return self.__width       
    
    def get_length(self):        
        return self.__length

    def area(self):
        return self.__width * self.__length

    def perimeter(self):
        return 2 * (self.__width + self.__length)

rectangle = Rectangle()
rectangle.set_length(20)
print(rectangle.get_length())
rectangle.set_length(5)
print(rectangle.get_length())
rectangle.set_length('sdf')
print(rectangle.get_length())

print('=====================')

rectangle.set_width(20)
print(rectangle.get_width())
rectangle.set_width(6)
print(rectangle.get_width())
rectangle.set_length('sdf')
print(rectangle.get_length())

print('=====================')

print(rectangle.area())
print(rectangle.perimeter())