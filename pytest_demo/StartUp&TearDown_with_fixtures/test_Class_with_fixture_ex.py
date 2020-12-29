import pytest

pytestmark = [pytest.mark.be, pytest.mark.slow]

@pytest.fixture(scope='module')
def setup_in_class():
    print()
    print(">>>>>>>>>>Initial setup for module is here <<<<<<<<<")
    return {'id': 20, 'name': "Madhu from Class"}

@pytest.mark.class_with_fixture
class TestDemo_pytest_class(object):

    def test_checkout_as_guest(self,setup_in_class):
        print("Checked out as a guest")
        print("Class: TestDemo_Pytest_class--1")
        print("Name :{}".format(setup_in_class.get('name')))

    def test_checkout_as_existing_user(self):
        print("Checked out as an existing user")
        print("Class: TestDemo_Pytest_class--2")
