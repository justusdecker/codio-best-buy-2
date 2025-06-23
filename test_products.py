from products import Product, NonStockedProduct, LimitedProduct
import pytest
def test_create_product():
    #Test that creating a normal product works.
    Product("test", price=1450, quantity=100)
def test_create_product_with_invalid_details():
    #Tests that creating a product with invalid details (empty name, negative price) invokes an exception.
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=1, quantity=-1)
def test_buy_to_much():
    #Test that buying a larger quantity than exists invokes exception.
    PRODUCT = Product('Test',10,1)
    with pytest.raises(ValueError):
        PRODUCT.buy(2)
def test_product_becomes_inactive():
    # Test that when a product reaches 0 quantity, it becomes inactive.
    PRODUCT = Product('Test',10,1)
    PRODUCT.buy(1)
    assert not PRODUCT.is_active()
def test_buy_modifies_quantity():
    # Test that product purchase modifies the quantity and returns the right output.
    PRODUCT = Product('Test',10,3)
    assert PRODUCT.buy(1) == PRODUCT.price
    assert PRODUCT.quantity == 2
def test_create_limited_product():
    LimitedProduct("Shipping", price=10, quantity=250, max_allowed_quantity=1)
def test_create_non_stock_product():
    NonStockedProduct("Windows License", price=10)
def test_buy_nonstock_no_below_zero():
    PRODUCT = NonStockedProduct("Windows License", price=10)
    PRODUCT.buy(10)
    assert PRODUCT.get_quantity() == 0
def test_buy_max_allowed_limited():
    PRODUCT = LimitedProduct("Shipping", price=10,quantity=10, max_allowed_quantity=1)
    with pytest.raises(ValueError):
        PRODUCT.buy(10)