
import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]

@pytest.mark.smoke
def test_valid_user():
    print("this is valid user")
    print("from Function : test_valid_user")
    print("This is marked for smoke test")
    print("In Pytest, mark is nothing but Tag in cucumber")

@pytest.mark.regression
def test_invalid_user():
    print("this is to test invalid user")
    print("from Function : test_invalid_user")
    print("This is marked for Regression")
    # assert 1 == 2, 'one is not two'
