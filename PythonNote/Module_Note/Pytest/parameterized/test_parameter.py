from string_num import greting as greetlib
from string_num import square_calculate as squarelib
                
import pytest
# def test_square_1():
#     result=squarelib(5)
#     assert result == 25

# def test_square_2():
#     result=squarelib(9)
#     assert result == 81

# def test_gretting_1():
#     name=greetlib("James")
#     assert name == "James"
# def test_gretting_2():
#     name=greetlib("Anna")
#     assert name == "Anna"

@pytest.mark.parametrize("test_input, expected_output",
                         [
                            ("sam", "sam"), 
                            ("john", "john"),
                            ("emily", "emily")
                        ])
def test_greeting(test_input, expected_output):
    name= greetlib(test_input)
    assert name==expected_output


@pytest.mark.parametrize("test_input, expected_output",
                         [
                            (2, 4), 
                            (9,81),
                            (4,16)
                        ])    
def test_square(test_input, expected_output):
    result= squarelib(test_input)
    assert result==expected_output