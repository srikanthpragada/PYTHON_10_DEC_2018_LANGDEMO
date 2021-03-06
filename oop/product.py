class Product:
    # class method
    @classmethod
    def create(cls, id, name):
        return cls(id, name)

    # Class attributes
    taxrate = 15

    @staticmethod
    def set_taxrate(newrate):
        if newrate > 0:
            Product.taxrate = newrate

    # Constructor
    def __init__(self, id, name, price=None, qoh=0):
        # Object attributes
        self.id = id
        self.name = name
        self.price = price
        self.qoh = qoh

    # Methods
    def print_details(self):
        print(self.id, self.name, self.price, self.qoh)

    def sell(self, qty):
        """
        Handles sale of product. Decrements quantity on hand by the qty sold

        Args:
           qty -  Quantity sold

        Returns:
           None
        """

        if qty <= self.qoh:
            self.qoh -= qty
        else:
            raise ValueError('Insufficient Stock!')

    def purchage(self, qty):
        self.qoh += qty

    @property
    def netprice(self):
        return self.price + (self.price * Product.taxrate / 100)

    # Special Methods
    def __str__(self):
        return f"{self.id} - {self.name} - {self.price} - {self.qoh}"

    def __eq__(self, other):
        print("__eq__")
        return self.id == other.id

    def __gt__(self, other):  # p1 > p2
        return self.price > other.price

    def __int__(self):
        return self.price
