from fact import solution

def test_factorial_positive():
    assert solution(10) == 55

def test_factorial_negative():
    assert solution(-1) == -1

def test_factorial_Zero():
    assert solution(0) == -1


