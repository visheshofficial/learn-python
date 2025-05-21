"""Kettle Module"""


class Kettle(object):
    """Class representing a kettle"""

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


kenwood=Kettle("Mile",13.45)
print(kenwood.make)
print(kenwood.price)
print(kenwood.on)
print(kenwood)
kenwood.price=13.90
print(kenwood.price)
