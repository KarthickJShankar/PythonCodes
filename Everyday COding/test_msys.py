import pytest
from msys import is_palindrom

def test_palindrom_positive():
    assert is_palindrom(111) == True

def test_palindrom_negative():
    assert is_palindrom(123) == False
