import pytest

import division

def test_division():
    assert division.Solution(4,2) == 2.0
    assert division.Solution(1, 2) == 0.5
    assert division.Solution(0,1) == 0.0
    with pytest.raises(ZeroDivisionError):
         division.Solution(1,0)
