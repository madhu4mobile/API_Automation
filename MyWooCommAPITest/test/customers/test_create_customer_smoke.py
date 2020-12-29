import pytest
import logging as logger

from MyWooCommAPITest.src.utilities.genericUtilities import util_to_generate_random_email_and_password
from MyWooCommAPITest.src.helpers.customers_Helper import CustomerHelper


@pytest.mark.testId_C1_11
def test_create_customer_with_only_email_and_password():
    logger.info("Test : C1 - Testing create customer with only email and password")
    logger.debug("just to test logger.debug message appearance")

    random_email_with_pw = util_to_generate_random_email_and_password()
    logger.info(random_email_with_pw)

    email = random_email_with_pw['email']
    password = random_email_with_pw['password']

    # create payload
    payload = {'email': email, 'password': password}

    # make the call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    #import pdb; pdb.set_trace() # to set a breakpoint

    # verify status code of the call

    # verify email in the response

    # verify customer is created in database

    # tear down to delete the email created - to maintain database tidy.
