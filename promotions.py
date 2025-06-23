from abc import ABC, abstractmethod
from math import ceil
class Promotion(ABC):
    """
    Abstract base class for all product promotions.

    Concrete promotion classes must inherit from this class and implement
    the `apply_promotion` method.
    """
    def __init__(self, name: str):
        if not isinstance(name, str) or not name:
            raise ValueError("The promotion name must be a non-empty string.")
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """
        Applies the promotion logic to calculate the discounted price for a given product and quantity.
        """
        pass
class BOGO(Promotion):
    """
    Promotion: Buy one, get one free (BOGO).
    For every two items purchased, one is free.
    """
    def __init__(self):
        super().__init__("Buy 1, get 1 free")

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Calculates the price for the "Buy 1, Get 1 Free" promotion.
        You pay for every second item.
        Example: Quantity 1 -> pays for 1
                Quantity 2 -> pays for 1
                Quantity 3 -> pays for 2
                Quantity 4 -> pays for 2
        """
        if quantity <= 0:
            return 0.0
        # Berechnet, wie viele Artikel tatsächlich bezahlt werden müssen.
        # Für je 2 Artikel zahlt man für 1. Also: bezahlte_menge = ceil(menge / 2)
        paid_quantity = ceil(quantity / 2)
        return paid_quantity * product.price

class SecondHalfPrice(Promotion):
    """
    Promotion: Second item at half price.
    Every second item purchased is half price.
    """
    def __init__(self):
        super().__init__("Second item half price")

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Calculates the price for the "Second Item Half Price" promotion.
        """
        if quantity <= 0:
            return 0.0

        # Anzahl der Paare (wobei ein Artikel zum vollen Preis, einer zum halben Preis ist)
        num_pairs = quantity // 2
        # Verbleibende Artikel (wenn die Menge ungerade ist)
        remaining_items = quantity % 2

        total_price = (num_pairs * product.price) + \
                      (num_pairs * product.price * 0.5) + \
                      (remaining_items * product.price)
        return total_price

class PercentDiscount(Promotion):
    """
    Promotion: Applies a fixed discount amount to the total price.
    """
    def __init__(self, discount_amount: float):
        if not isinstance(discount_amount, (int, float)) or discount_amount < 0:
            raise ValueError("The discount amount must be a non-negative number.")
        super().__init__(f"Fixed discount: ${discount_amount:.2f}")
        self.discount_amount = discount_amount

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Calculates the price after applying a fixed discount.
        The price will not fall below zero.
        """
        if quantity <= 0:
            return 0.0
        total_price_before_discount = quantity * product.price
        return total_price_before_discount - ((self.discount_amount*.01) * total_price_before_discount)