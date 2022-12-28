"""
COMP.CS.100
Tekijä: Patrick Selin
Opiskelunumero: tuni.fi:xxxxxx
Tehtävä: 10.4
"""
ALE = 0.00
class Product:
    """
    The template describes a simple class Product which can be
    used to handle products available in a store.
    Every product has three properties:

    name (str)
    price (float)
    sale percentage (float)
    """

    def __init__(self, name, price, sale_p=ALE):
        """
        :param name: str, price: float, sale_p: float
        """
        self.__name = name
        self.__price = price
        self.__sale_p = sale_p

    def set_sale_percentage(self, sale_p):
        """
        method set_sale_percentage, which can be used to put
        the product on sale with the given sale percentage
        """
        self.__sale_p = sale_p

    def get_price(self):
        """
        metodi get_price, which returns the current sale price
        of the product, which is either the original price or
        cheaper if sale percentage is not 0.0.
        """
        sale_p_des = ( 100 - self.__sale_p ) /100
        sale_price = self.__price * sale_p_des

        return sale_price

    def printout(self):
        """
        Prints the info.
        """
        print(self.__name)
        print("  price:", self.__price)
        print("  sale%:", self.__sale_p)

def main():

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()