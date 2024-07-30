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

## package  
- Install: 
	- please install pip install pytest 
- Import libary
	- pytest import `import pytest -vs`
	- mock import `from unittest.mock import Mock`
- pytest command to run use either method
	- default `pytest`
	- specific unit test `pytest -vs test_shoppingcart.py`
	
