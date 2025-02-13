import pytest

@pytest.mark.xfail(reason='expected to fail')
def testLogin() :
    assert 4 == 5

@pytest.mark.filterwarnings
def testLogoff():
    print('Logout successful')

@pytest.mark.skip
def testCalculation():
    assert 2 + 2 == 4