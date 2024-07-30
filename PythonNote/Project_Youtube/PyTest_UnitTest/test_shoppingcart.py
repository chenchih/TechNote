from shoppingcart import ShoppingCart
from item_db import ItemDatabase
from unittest.mock import Mock
import pytest

@pytest.fixture
def cart():
    #all setup
    return ShoppingCart(5)

def test_can_add_item_to_cart(cart):
    #adding to chart
    #cart=ShoppingCart(5)
    cart.add('apple')
    assert cart.size() == 1

def test_when_item_added_then_cart_contains_items(cart):
    #cart=ShoppingCart(5)
    cart.add('apple')
    assert "apple" in cart.get_items()

def test_when_add_morethan_max_should_fail(cart):
    #cart=ShoppingCart(5)
    # if throw this error mean pass
    # if you run this will not catch the bug if self.max_size-1
    # with pytest.raises(OverflowError):
    #     for i in range(6):
    #         cart.add('apple')

#     #run 5 times
    for i in range(5):
        cart.add('apple')
    with pytest.raises(OverflowError):
        cart.add('apple')

def test_togetthe_price(cart):
    cart.add('apple')
    cart.add('banana')
    price_map={ 'apple': 4.0,'banana': 1.0 }
    assert cart.get_total_price(price_map) == 5.0

def test_togetthe_price_mock(cart):
    #cart= ShoppingCart(5)
    cart.add('apple')
    cart.add('banana')
    item_database=ItemDatabase()
    #mock 
    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        if item == "banana":
            return 2.0
        
    item_database.get = Mock(side_effect=mock_get_item)
    assert cart.get_total_price(item_database) == 3.0

    