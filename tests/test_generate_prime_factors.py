# pylint: disable=missing-docstring
"""
The test module for Prime Factors
"""
import pytest # import pytest
from primefactorization import generate_prime_factors

def test_string_invalid_arguments():
    """When data type is float, type that is not valid then a ValueError is raised. """
    #assert generate_prime_factors('string123') == []
    with pytest.raises(ValueError):
        #generate_prime_factors('string123')
        generate_prime_factors(str)

def test_float_invalid_arguments():
    """When data type is float, type that is not valid then a ValueError is raised. """
    #assert generate_prime_factors(1.11) == []
    with pytest.raises(ValueError):
        #generate_prime_factors(1.11)
        generate_prime_factors(float)

def test_when_argument_is_1():
    """when argument is 1, then an empty list is returned """
    assert generate_prime_factors(1) == []
