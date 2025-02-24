import pytest
import sys
import math 
@pytest.mark.skip(reason="I don't need this right now")
def test_welcome():
    print ("hello world")

@pytest.mark.skipif(sys.version_info<(3,10), reason="version not match, unable to test")
def test_welcome_name():
    print ("hello world Test, How are you doing")


def test_hello():
    print("This is a skip marker test")

@pytest.mark.xfail
def test_Calculation():
    assert 2 + 2 == 6
