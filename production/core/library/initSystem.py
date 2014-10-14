# coding: utf-8

from production.product.models import TypeProduct


class InitSystem():

    """
            Class responsible to implement all methods to initialization
    """

    def __init__(self):
        self.initializeTypeProduct()

    def initializeTypeProduct(self):
        """
            Must be initilize the TypeProduct class with some values
            # Access Point / Access points
            # Switch / Switches
        """

        TypeProduct(id=1, name='Access Point',
                    description='Access points').save()

        TypeProduct(id=2, name='Switch',
                    description='Switches').save()
