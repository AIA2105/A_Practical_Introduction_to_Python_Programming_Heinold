class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, n):
        self.make_purchase(n)
        if 0 < n < 10:
            return self.price * n
        elif 10 <= n < 100:
            return (self.price - self.price * 0.1) * n
        else:
            return (self.price - self.price * 0.2) * n

    def make_purchase(self, n):
        if n <= self.amount:
             self.amount = self.amount - n
             return self.amount

p1=Product('tomato',100,5)
p2=Product('banana',50,10)


print(p1.get_price(20))
print(p1.amount)
print(p2.get_price(20))
print(p2.amount)