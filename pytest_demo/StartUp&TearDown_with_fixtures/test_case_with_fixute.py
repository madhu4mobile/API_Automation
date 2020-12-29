import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]

@pytest.fixture(scope='module')
def startup_setup():
    print()
    print(">>>>>>>>>>Initial setup for module is here <<<<<<<<<")
    return {'id': 20, 'name': "Madhu"}


@pytest.mark.smoke
@pytest.mark.temp
def test_valid_user(startup_setup):
    print("this is valid user")
    print("from Function : test_valid_user")
    print("This is marked for smoke test")
    print("In Pytest, mark is nothing but Tag in cucumber")
    # import pdb; pdb.set_trace()  # to set a break point
    print("This uses name '{}' from startup_setup module".format(startup_setup.get('name')))


@pytest.mark.regression
def test_invalid_user():
    print("this is to test invalid user")
    print("from Function : test_invalid_user")
    print("This is marked for Regression")
    #assert 1 == 2, 'one is not two'
