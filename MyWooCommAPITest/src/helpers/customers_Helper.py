

from MyWooCommAPITest.src.utilities.genericUtilities import util_to_generate_random_email_and_password
from MyWooCommAPITest.src.utilities.requestsUtility import requestUtility

class CustomerHelper(object):

    def __init__(self):
        self.request_utility = requestUtility()

    def create_customer(self,email=None, password=None, **kwargs):
        if not email: # in the case when email is not provided, we use the helper to generate a random email for us
            email = util_to_generate_random_email_and_password('email')
        if not password:
            password = 'Password1'

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)

        create_user_json = self.request_utility.post('customers',payload=payload,expected_status_code=201)
        return True




