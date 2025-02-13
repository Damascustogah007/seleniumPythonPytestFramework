import pytest

@pytest.fixture(scope="class", autouse=True) #Arrange
def setUp():
    print('Setup')
    print("Launch browser")
    print("Login")
    print('Browse Product')
    yield
    print('Tear down')
    print('Browser close')