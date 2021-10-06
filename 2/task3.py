class Product:
    def __init__(self, description, price, length, width):
        if not isinstance(description, str) or not isinstance(price, int):
            raise TypeError('TypeError')
        self.__description = description
        self.__price = price  
        self.__length = length  
        self.__width = width

    def __str__(self):
        return f'Name of product: {self.__description}\nPrice of product: {self.__price}\n'

    def get_price(self):
        return self.__price

    def get_description(self):
        return self.__description

class Customer:
    def __init__(self, name, surname, phone_number):
        if not isinstance(name, str) or not isinstance(surname, str) or not isinstance(phone_number, int):
            raise TypeError('TypeError')
        self.__name = name
        self.__surname = surname  
        self.__phone_number = phone_number

    def __str__(self):
        return f'Customer info: {self.__name} {self.__surname}, +{self.__phone_number}' 

class Order:
    def __init__(self, customer, products):
        if not isinstance(customer, Customer) or not isinstance(products, list):
            raise TypeError('TypeError')
        self.__customer = customer
        self.__products = products
        self.__order_price = 0

    def __str__(self):
        descriotion_of_products = ''
        for product in self.__products:
            descriotion_of_products += f'Name of product: {product.get_description()}\nPrice of product: {product.get_price()}$\n'
        return f'Оrder description:\nPrice of order: {self.__order_price}$\n{self.__customer}\n{descriotion_of_products}\n-------------------\n'

    def count_price(self):
        self.__order_price = 0
        for product in self.__products:
            self.__order_price += product.get_price()
        return self.__order_price


def main():
    try:
        customer1 = Customer('Vitala', 'Kovalov', +380978557148)
        laptop = Product('Laptop', 100, 40, 50)
        phone = Product('Samsung', 50, 20, 15)
        powerbank = Product('Powerbank', 5, 15, 15)
        order1 = Order(customer1, [laptop, phone, powerbank])
        order1.count_price()
        print(order1)

        customer2 = Customer('Roma', 'Tkachenko', +380978557149)
        car = Product('Car', 5000, 500, 250)
        bike = Product('Bike', 400, 200, 35)
        order2 = Order(customer2, [car, bike])
        order2.count_price()
        print(order2)

        return 'All is good!'
    except:
        return 'Something went wrong!'

print(main())