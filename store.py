from products import Product
class Store:
    """
    A Class that will manage Products
    """
    def __init__(self):
        self.products = [
            Product("Bose QuietComfort Earbuds", price=250, quantity=500),
            Product("MacBook Air M2", price=1450, quantity=100),
            Product("A Big Tasty Bacon", price=250, quantity=500)] #I'm hungry 🤤
    def remove_product(self,product: Product):
        """ Remove a given Product from ``products`` """
        self.products.remove(product)
    def get_total_quantity(self) -> int:
        """ Get all products quantity """
        return sum([i.get_quantity() for i in self.products])

    def get_all_products(self) -> list:
        """ Get all active products """
        return [i for i in self.products]
    def order(self, product: tuple[Product, int]):
        """ Take an order by calling for each element in product the buy method of a Product Instance! """
        return sum([prod.buy(quan) for prod, quan in product])
