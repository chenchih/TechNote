import pytest

@pytest.fixture
def setup():
    print("Lanuch Browser")
    print("Login")
    print("Browser Product")
    yield
    print("Logout")
    print("Close browser")
    
def testAllitemtoChart(setup):
    print("Login Success")

def removeItemfromChart():
    print("Logout Success")