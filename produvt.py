class Product:
    taxrate = 12
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Name : {self.name}, Price : {self.price}"

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    def __gt__(self, other):
        #print("__gt__")
        return self.price > other.price

    @property
    def sellingprice(self):
        return self.price + self.price * Product.taxrate / 100


p1 = Product("A", 10000)
print(p1.sellingprice)

p2 = Product("B", 5000)
p3 = Product("A", 10000)
p4 = Product("C", 2500)

print(p1 == p3)  # p1.__eq__(p3)
print(p1 == p2)
print(p1)  # str(p1)  -> p1.__str__()

print(p1 > p2)  # p1.__gt__(p2)
print(p1 < p2)

lp = [p1, p2, p3, p4]
for p in sorted(lp):
    print(p)