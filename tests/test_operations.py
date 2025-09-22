import pytest
from app.operations import addition, subtraction, multiplication, division

def test_addition():
    assert addition(2, 3) == 5

def test_subtraction():
    assert subtraction(5, 3) == 2
    
def test_multiplication():
    assert multiplication(4, 3) == 12
    
def test_division_positive():
    assert division(10, 2) == 5

def test_division_by_zero():
    with pytest.raises(ValueError):
        division(10, 0)
