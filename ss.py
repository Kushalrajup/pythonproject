import pytest
@pytest.fixture
def values():
    add1=10
    diff1=0
    return [add1,diff1]

def test_method1(values):
    a=5
    b=5
    s=a+b
    assert values[0]==s,"failure"
@pytest.mark.skip
def test_method2(values):
    x=6
    y=4
    d=x-y
    assert values[1]==d,"FAilure"
@pytest.mark.xfail
def test_method3(values):
    a=5
    b=5
    s=a+b
    assert values[0]==s+2,"failure"