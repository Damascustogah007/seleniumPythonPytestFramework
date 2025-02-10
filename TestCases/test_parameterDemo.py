import pytest
@pytest.mark.parametrize('name, role', [('Charles', 'QA'), ('Mary', 'dev'), ('Steve', 'PO')])

def test_validation(name, role):
    assert name is not None
    assert role is not None

@pytest.fixture(scope="module", params=["https://www.google.com", "https://www.google.com"])
def val(request) :
    return request.param

def test_val(val) :
    assert val is not None