class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative")
        else:
            self._price = value
    @price.deleter
    def price(self):
        print("Price is being deleted")
        del self._price

x = Product(50)
print(x.price)
x.price = 100
print(x.price)
del x.price