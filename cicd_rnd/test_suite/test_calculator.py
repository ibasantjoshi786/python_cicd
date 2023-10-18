import pytest
from cicd_rnd.source import calculator as calci


@pytest.mark.parametrize('no1, no2, expected_result', [(8, 3, 11), (4, 2, 6)])
def test_addition(no1, no2, expected_result):
    # This is the function to test add functionality
    result = calci.addition(no1, no2)
    assert result == expected_result


@pytest.mark.parametrize('no1, no2, expected_result', [(8, 3, 5), (4, 2, 2)])
def test_subtraction(no1, no2, expected_result):
    # This function is used for testing subtraction code
    result = calci.subtraction(no1, no2)
    assert result == expected_result


@pytest.mark.parametrize('no1, no2, expected_result', [(8, 3, 24), (4, 2, 8)])
def test_multiplication(no1, no2, expected_result):
    # This function is used to test multiplication
    result = calci.multiplication(no1, no2)
    assert result == expected_result


@pytest.mark.parametrize('no1, no2, expected_result', [(8, 4, 2), (6, 2, 3)])
def test_divide(no1, no2, expected_result):
    result = calci.divide(no1, no2)
    assert result == expected_result
