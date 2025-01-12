import pytest
from fuel import convert, gauge

def main():
    test_correct_input()
    test_zero_division()
    test_value_error()


def test_correct_input():
    # Test valid inputs and their expected outputs
    assert convert('1/4') == 25 and gauge(25) == '25%'
    assert convert('1/100') == 1 and gauge(1) == 'E'
    assert convert('99/100') == 99 and gauge(99) == 'F'

def test_zero_division():
    # Test division by zero
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_value_error():
    with pytest.raises(ValueError):
        convert('cat/dog')

if __name__ == "__main__":
    main()