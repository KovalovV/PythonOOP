# Pizzeria offers pizza-of-the-day for business lunch. 
# The type of pizza-of-the-day depends on the day of week. 
# Having a pizza-of-the-day simplifies ordering for customers. 
# They don't have to be experts on specific types of pizza. 
# Also, customers can add extra ingredients to the pizza-of-the-day. 
# Write a program that will form orders from customers.

import datetime
import json

class Pizza:
    def __init__(self, name, price, diametr, ingredients):
        self.name = name
        self.price = price  
        self.diametr = diametr  
        self.ingredients = ingredients

    def __str__(self):
        return f'Name of pizza: {self.name}\nPrice of pizza: {self.price}\n'

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def diametr(self):
        return self.__diametr

    @property
    def ingredients(self):
        return self.__ingredients

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Invalid input data type')
        if not len(name):
            raise ValueError('Incorrect data input values')
        self.__name = name

    @price.setter
    def price(self, price):
        if not isinstance(price, str):
            raise TypeError('Invalid input data type')
        if float(price) <= 0:
            raise ValueError('Incorrect data input values')
        self.__price = price

    @diametr.setter
    def diametr(self, diametr):
        if not isinstance(diametr, str):
            raise TypeError('Invalid input data type')
        if float(diametr) <= 0:
            raise ValueError('Incorrect data input values')
        self.__diametr = diametr

    @ingredients.setter
    def ingredients(self, ingredients):
        # if not isinstance(ingredients, str):
        #     raise TypeError('Invalid input data type')
        # if not len(ingredients):
        #     raise ValueError('Incorrect data input values')
        self.__ingredients = ingredients

class Katyusha(Pizza):
    def __init__(self, name, price, diameter, ingredients):
        super().__init__(name, price, diameter, ingredients)

class Pepperoni(Pizza):
    def __init__(self, name, price, diameter, ingredients):
        super().__init__(name, price, diameter, ingredients)

class Manhattan(Pizza):
    def __init__(self, name, price, diameter, ingredients):
        super().__init__(name, price, diameter, ingredients)

class Texas(Pizza):
    def __init__(self, name, price, diameter, ingredients):
        super().__init__(name, price, diameter, ingredients)

class Barbecue(Pizza):
    def __init__(self, name, price, diameter, ingredients):
        super().__init__(name, price, diameter, ingredients)

class Carbonara(Pizza):
    def __init__(self, name, price, diameter, ingredients):
        super().__init__(name, price, diameter, ingredients)

class Bavarian(Pizza):
    def __init__(self, name, price, diameter, ingredients):
        super().__init__(name, price, diameter, ingredients)

class Customer:
    def __init__(self, name, surname, phone_number):
        self.name = name
        self.surname = surname  
        self.phone_number = phone_number

    @property
    def name(self):
        return self.__name

    @property
    def phone_number(self):
        return self.__phone_number

    @property
    def surname(self):
        return self.__surname

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Invalid input data type')
        if not len(name):
            raise ValueError('Incorrect data input values')
        self.__name = name

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError('Invalid input data type')
        if not len(surname):
            raise ValueError('Incorrect data input values')
        self.__surname = surname

    @phone_number.setter
    def phone_number(self, phone_number):
        if not isinstance(phone_number, str):
            raise TypeError('Invalid input data type')
        if len(phone_number) < 10:
            raise ValueError('Incorrect data input values')
        self.__phone_number = phone_number

    def __str__(self):
        return f'Customer info: {self.name} {self.surname}, +{self.phone_number}' 

class Order:
    with open('C:/MinGW/bin/cpp/Python/3/pizza_of_day.json') as pizza_of_day:
        data_of_pizzas = json.load(pizza_of_day)

    pizzas_of_day = [Katyusha(data_of_pizzas['0']['name'], data_of_pizzas['0']['price'], data_of_pizzas['0']['diametr'], data_of_pizzas['0']['ingradients']),
                    Pepperoni(data_of_pizzas['1']['name'], data_of_pizzas['1']['price'], data_of_pizzas['1']['diametr'], data_of_pizzas['1']['ingradients']),
                    Manhattan(data_of_pizzas['2']['name'], data_of_pizzas['2']['price'], data_of_pizzas['2']['diametr'], data_of_pizzas['2']['ingradients']),
                    Texas(data_of_pizzas['3']['name'], data_of_pizzas['3']['price'], data_of_pizzas['3']['diametr'], data_of_pizzas['3']['ingradients']),
                    Barbecue(data_of_pizzas['4']['name'], data_of_pizzas['4']['price'], data_of_pizzas['4']['diametr'], data_of_pizzas['4']['ingradients']),
                    Carbonara(data_of_pizzas['5']['name'], data_of_pizzas['5']['price'], data_of_pizzas['5']['diametr'], data_of_pizzas['5']['ingradients']),
                    Bavarian(data_of_pizzas['6']['name'], data_of_pizzas['6']['price'], data_of_pizzas['6']['diametr'], data_of_pizzas['6']['ingradients'])]

    with open('C:/MinGW/bin/cpp/Python/3/ingradients.json') as ingradients_in_stock:
        data_of_ingradients = json.load(ingradients_in_stock)

    def __init__(self, customer, ingredients):
        self.customer = customer
        self.ingredients = ingredients
        self.__day_of_week = datetime.datetime.today().isoweekday()
        self.__pizza = Order.pizzas_of_day[self.__day_of_week - 1]

    @property
    def customer(self):
        return self.__customer

    @property
    def ingredients(self):
        return self.__ingredients

    @customer.setter
    def ingredients(self, ingredients):

        if not all(bool(Order.data_of_ingradients[ingredient]) for ingredient in ingredients):
            raise KeyError('There is no such ingredient')
        #     # перевірка на наявність таких продуктів на складі
        self.__ingredients = ingredients

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError('Invalid input data type')
        self.__customer = customer
        
    def __str__(self):
        return f"""Оrder description:\nPrice of order: {self.count_price()}$\n{self.__customer}\nName of pizza: {self.__pizza.name}\nIngradients of pizza: {", ".join(self.__pizza.ingredients)}\nDiametr of pizza: {self.__pizza.diametr} sm\n-------------------\n"""

    def count_price(self):
        self.__order_price = float(self.__pizza.price)
        for ingredient in self.__ingredients:
            self.__pizza.ingredients.append(ingredient)
            self.__order_price += float(Order.data_of_ingradients[ingredient]['price'])
        return self.__order_price


def main():
    try:
        customer1 = Customer('Vitala', 'Kovalov', '0978557148')
        order1 = Order(customer1, ["bananas", "pepperoni", "barbecue sauce"])
        print(order1)
    except:
        raise KeyError('There is no such ingredient')
    

main()