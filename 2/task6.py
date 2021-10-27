class Node:
    """
    Class Node. Describes the node of a binary tree.
    """

    def __init__(self, id, price):
        if not isinstance(id, int) or not isinstance(price, (int, float)):
            raise TypeError('Invalid input data type')
        if price <= 0:
            raise ValueError('Incorrect data input values')
        self.left = None
        self.right = None
        self.id = id
        self.price = price

    def insert(self, id, price):
        """
        Method insert(price).
        Gets the ID of the product and its quantity
        """

        if self.id:
            if id < self.id:
                if not self.left:
                    self.left = Node(id, price)
                else:
                    self.left.insert(id, price)
            elif id > self.id:
                if not self.right:
                    self.right = Node(id, price)
                else:
                    self.right.insert(id, price)
        else:
            self.id = id

    def find_id(self, key):
        """
        Method find_id(key).
        Receives the product key and returns its price
        """

        if key < self.id:
            if not self.left:
                raise Exception('Not find such product')
            return self.left.find_id(key)
        elif key > self.id:
            if not self.right:
                raise Exception('Not find such product')
            return self.right.find_id(key)
        else:
            return self.price

def cout_price(root, product_id, amount):
    """
    Method cout_price(product_id, amount).
    Receives the product key, product quantity and returns the price of the entire order
    """
    return root.find_id(product_id) * amount

def main():
    try:
        root = Node(12, 80)
        root.insert(6, 50)
        root.insert(14, 40)
        root.insert(3, 100)
        root.insert(13, 110)
        product_id, amount = list(map(int, input('Put the product ID and the amount here: ').split()))
        print(f'Price: {cout_price(root, product_id, amount)}')
        return ' #All is good!'
    except Exception:
        return ' #Not find such product'

print(main())