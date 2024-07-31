# Note for Run UnitTest using pytest

## Reference
- This tutorial is base on [Youtube Channel:pixegami](https://www.youtube.com/playlist?list=PLZJBfja3V3RvxooZ5SNOr7CMFzURr4NBs) on `How To Write Unit Tests in Python • Pytest Tutorial`
- [mock documentation](https://docs.python.org/3/library/unittest.mock.html)


## Introuction
This tutorial conver most of createing a unittest using Pytest. I really think it a good tutorial on teaching how to write unitest.
In this tutorial it cover on pytest:
- fixture: for duplicate code, so since it a class, we need to inital an object `cart=ShoppingCart(5)`, so need to reuse the code. This can be fixture as setup, since it need to inital on every test. 
- mock:  mock object is a simulated object used in testing to isolate the component you're testing.

I really like his explanation on the mock that if you need to use a function that is implment by other developer, but it's not ready yet, you can use the `mock` and stimulate. 

## UnitTest/ TEST Case
In Case1~Case5 will use `shoppingcart.py`, and `test_shoppingcart.py`, but in case5 will also use `item_db.py` which is the fake database
- Case1: add an item
- Case2: check cart contain item
- Case3: Trigger Exception Error when meet max value
- Case4: Total Up Price 
- Case5: Total Up Price with Mock using a fake database

In Note 5 create a fake database which have a get method, but the get method, just think it's implement by other people, and not done yet. So If you are person to write Unittest, then you need to test it. So you will need a mock to validate your unittest. 


### Case1:
Will add an item and check the size 

- You can use either `self.items = []` or `self.items:List[str]=[]` they are all the same. 
- will add item into list: `self.items.append(item)` 
- Get the size of the list: `return len(self.items)`
- Validate whether `size = 1`: `assert cart.size() == 1`

It will add an apple into list, and return the size of the list, which in this case is `1`


> `shoppingcart.py`

```
from typing import List
class ShoppingCart:
    def __init__(self)-> None:
        #self.items = []
        self.items:List[str]=[]
        
    def add(self, item: str):
       self.items.append(item)

    def size(self)-> int:
        return len(self.items)
```

> `test_shoppingcart.py`
```
from shoppingcart import ShoppingCart
import pytest

def test_can_add_item_to_cart():
    #adding to chart
    cart=ShoppingCart()
    cart.add('apple')
    assert cart.size() == 1
```

### Case2:
Validate the item is `apple`

**Note:** I will not include all code, the `...` means same as above
- return the list items: `return self.items`
- validate item in list: `assert "apple" in cart.get_items()`


### Case3:
Validate when cart is full must trigger exception error. 

- Adding max_value:  `self.max_size=max_size`
- raise exception: `pytest.raises(OverflowError)`

> `shoppingcart.py`
```
class ShoppingCart:
    def __init__(self, max_size: int)-> None:
        #self.items = []
        self.items:List[str]=[]
        self.max_size=max_size
    
    def add(self, item: str):
        #check size with max_size, if same then raise error
        if self.size()== self.max_size- 1:
            raise OverflowError("Cannot add more items")
        #else continue adding
        self.items.append(item)
```

#### Will Not Trigger Exception when reach MAX

In `shoppingcart.py`, when using `if self.size()== self.max_size -1` will not catch the exception not trigger Error, it will still be pass. 
The reason is because of this code below, when you add all item full into cart, but the 6th time will not be execute, so indeed this test will fail. 
- When `Size=0` and `max_value=5-1` condition false so add item to list: The condition size == max_value - 1 is false, so the item is added.
- When `size=1` and `max_value=5-1` conditions false so add item to list: The condition is still false.
- When `size=4` and `max_value=5-1` condition true  so will not add to item: The condition is true, so the item is not added.
- when `size=5` and `max _value=5-1` condition false will not add, but because **check happen before add**, so **will not trigger error**: This is where the issue lies.

The problem is that the check happens before the item is added. So, when size is 5, the condition size == max_value - 1 is false. The cart is already full after the 4th item, so we need to add one more to cause an overflow. Please refer below solution to fix this problem
> `test_shoppingcart.py`
```
from shoppingcart import ShoppingCart
import pytest
def test_when_add_morethan_max_should_fail():
    cart=ShoppingCart(5)
    #if throw this error mean pass
	#if you run this will not catch the bug if self.max_size-1
    with pytest.raises(OverflowError):
        for i in range(6):
            cart.add('apple')
```

#### Solution to fix trigger exception

Just remove below code on `test_shoppingcart.py`: 
```
with pytest.raises(OverflowError):
        for i in range(6):
            cart.add('apple')
```
and change to below code and run the test

> `test_shoppingcart.py`
```
def test_when_add_morethan_max_should_fail():
    cart=ShoppingCart(5)
    # if throw this error mean pass
    # if you run this will not catch the bug if self.max_size-1
#     #run 5 times
    for i in range(5):
        cart.add('apple')
    with pytest.raises(OverflowError):
        cart.add('apple')
```
![case3_raiseerror](img/case3_error_solution.PNG)

Now when you run the case will fail, it catch the error. Now you can remove the `-1` and run the test will pass. 


### Case4:
Will sum the value of list , and do validate the items
- total up the list: `total_price+=price_map.get(item)`or `price_map[item]`.
	- since it's dictionary, can access using get method to get key value. 

> `shoppingcart.py`
```
from typing import List
class ShoppingCart:
    .....
    def get_total_price(self, price_map):
        total_price=0
        for item in self.items:
            total_price+=price_map.get(item) 
# you can also use index method price_map[item]
        return total_price
```

> `test_shoppingcart.py`
```
def test_togetthe_price():
    cart= ShoppingCart(5)
    cart.add('apple')
    cart.add('banana')
    price_map={ 'apple': 4.0,'banana': 1.0 }
    assert cart.get_total_price(price_map) == 5.0
```
![case4](img/case4.PNG)

### Cleaning Code for duplicate:
As you can see the unit test's code have alot of duplicate logic, you can use fixture to `fixture` for dupicate logic `cart= ShoppingCart(5)`.
![duplicate](img/duplicate.PNG)

To make the code clearer without adding same logic, you can create a cart is basically is the setup and add a fixture decorator. 
You can see define `cart()`, which meant all the intial cart will write over here. Now you have to do this: 
- create cart() function
- create pxtest.fixture
- pass all the argument with cart

![fixture](img/fixture.PNG)

> `shoppingcart.py`
```
@pytest.fixture
def cart():
    return ShoppingCart(5)

def test_can_add_item_to_cart(cart):

def test_when_item_added_then_cart_contains_items(cart):
    cart.add('apple')
    assert "apple" in cart.get_items()
```


### Mock with fake database
A mock object is a simulated object used in testing to isolate the component you're testing.

In previous we store data in dictionary, and we know we can use get method. But what if we want to use the get method, but it's not implement yet. In this test will create a fake database, and will have a get method. 
Just image if the get method is develope by other developer in our team and is not working yet, but you need to validate the unit test to make sure it work. In this situation we need to add get method to mock. To let the get method work, we need to mock, to stimulate get method work properly. 

>create a fake database that gave get method: `item_db.py` 
```
class ItemDatabase:
    def __init__(self)->None:
        pass
    def get(self, item: str)->float:
        pass

```
 
please import mock and ItemDatabase 
> `test_shoppingcart.py`
```
from shoppingcart import ShoppingCart
from item_db import ItemDatabase
from unittest.mock import Mock
import pytest
…. 
def test_togetthe_price(cart):
    cart.add('apple')
    cart.add('banana')
    cart.add('banana')
    item_database=ItemDatabase()
    assert cart.get_total_price(item_database) == 3.0
```
When you run this test it will Fail, instead of waiting for the get method to implement in order to relied on `item_database` or `ItemDatabase()`, we can use `mock` behavior of `item_database`.

#### Adding Mock 
- mock get method: `item_database.get = Mock()`

get method is not implement and still developer, so need to mock it like this:
>>　`item_database.get = Mock(return_value=1.0)`


> `test_shoppingcart.py`
```
def test_togetthe_price(cart):
    #cart= ShoppingCart(5)
    cart.add('apple')
    cart.add('banana')
    cart.add('banana')
    item_database=ItemDatabase()
    #mock 
    item_database.get = Mock(return_value=1.0)
    assert cart.get_total_price(item_database) == 3.0

```

Now when you run it will pass, and assert will pass. 
But the problem here is that I want to set specfic value for each item , not giving all the same value 1. 
In the above basically each item will have 1.0 so having three item  total up to 3.0 so indeed assert will pass. 

![mock](img/mock1.PNG)


#### Customize Mock
To customize the mock of the value, need to create a function and use side_effect argument. 
Let change the code liek below
> `test_shoppingcart.py`
```
def test_togetthe_price_mock(cart):
 ..... #same as above
    #mock 
    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        if item == "banana":
            return 2.0
        
    item_database.get = Mock(side_effect=mock_get_item)
    assert cart.get_total_price(item_database) == 3.0
```
Now as you can see to need to create a function, and need to add argument `side_effect` and assign the function to it. 
Now you can see I each item have it's own value, not like previous one have a fixed value. 

![mock_side_effect](img/mock2.PNG)

## package  
- Install: 
	- please install pip install pytest 
- Import libary
	- pytest import `import pytest -vs`
	- mock import `from unittest.mock import Mock`
- pytest command to run use either method
	- default `pytest`
	- specific unit test `pytest -vs test_shoppingcart.py`
	
