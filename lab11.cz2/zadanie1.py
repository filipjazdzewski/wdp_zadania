def f(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def test_f():
    assert f(5) == 120
    assert f(4) == 22
