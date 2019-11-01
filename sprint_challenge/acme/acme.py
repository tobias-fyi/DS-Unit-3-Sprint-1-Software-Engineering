"""
acme.acme :: Codified Acme Products
"""

from random import randint


class Product:
    """
    Represents a general Acme product.

    Parameters
    ----------
    name : string 
        Name of the Product; no default.
    price : integer 
        Selling price of the Product; default is $10.
    weight : integer 
        Product Weight; default is 20.
    flammability : float 
        Measure of the Product's flammability; default is 0.5.
    identifier : integer
        Auto-generated random (uniform) number between 1000000 and 9999999, inclusive.
    """

    def __init__(
        self,
        name,
        price=10,
        weight=20,
        flammability=0.5,
        identifier=randint(1000000, 9999999),
    ):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """Calculates price / weight ratio; returns a message stating stealability."""

        # Calculate the price / weight ratio
        pw_ratio = self.price / self.weight

        # Return message according to ratio
        if pw_ratio < 0.5:
            return "Not so stealable..."
        elif 0.5 <= pw_ratio < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        """
        Calculates the product of flammability and weight; returns a message. 
        """

        # Calculate `exp` : product of flammability and weight
        exp = self.flammability * self.weight

        # Return message options
        if exp < 10:
            return "...fizzle."
        elif 10 <= exp < 50:
            return "...boom!"
        else:
            return "...BABOOM!! No more Chinese laundry."
