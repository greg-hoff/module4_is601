import pytest
from typing import Union
from app.operations import Operations

Number = Union[int, float]

#-----------------------------------------------
# Testing for addition with parameterized inputs
#-----------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected", 
    [
        (2, 3, 5),
        (5, 3, 2),
        (4, 3, 12),
        (10, 2, 5),
    ]
    ids=[
        (2, 3, 5),           # Test adding two positive integers
        (0, 0, 0),           # Test adding two zeros
        (-1, 1, 0),          # Test adding a negative and a positive integer
        (2.5, 3.5, 6.0),     # Test adding two positive floats
        (-2.5, 3.5, 1.0),    # Test adding a negative float and a positive float
    ]
)
def test_addition(a: Number, b: Number, expected: Number):
    result = Operations.addition(a, b)
    assert result == expected, f"Expected {expected}, got {result}"
    
#-----------------------------------------------
# Testing for subtraction with parameterized inputs
#-----------------------------------------------    

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),           # Test subtracting a smaller positive integer from a larger one
        (0, 0, 0),           # Test subtracting two zeros
        (-5, -3, -2),        # Test subtracting a negative integer from another negative integer
        (10.5, 5.5, 5.0),    # Test subtracting two positive floats
        (-10.5, -5.5, -5.0), # Test subtracting two negative floats
    ],
    ids=[
        "subtract_smaller_positive_integer_from_larger",
        "subtract_two_zeros",
        "subtract_negative_integer_from_negative_integer",
        "subtract_two_positive_floats",
        "subtract_two_negative_floats",
    ]
)
def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    result = Operations.subtraction(a, b)
    assert result == expected, f"Expected {expected}, got {result}"
