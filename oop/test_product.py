from product import Product

p1 = Product(1, "iPhone X", 80000)  # Create object
print(p1.netprice)

p2 = Product(1, "iPhone X", 80000)  # Create object

print(id(p1),id(p2))

print(p1 == p2, p1 != p2)   # p1.__eq__(p2)

print(p1 > p2)   # p1.__gt__(p2)

print(int(p1))  #  p1.__int__()


