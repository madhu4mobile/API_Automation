import logging as logger
import random
import string


def util_to_generate_random_email_and_password(domain=None, email_prefix=None):
    logger.debug("Using helper util - create random email and random password")

    if not domain:
        domain = 'qatestapi.com'
    if not email_prefix:
        email_prefix = 'testemail'

    random_email_string_length = 10
    random_email_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))

    email = email_prefix + "_" + random_email_string + "@" + domain

    random_password_string_length = 20
    random_password = ''.join(random.choices(string.ascii_letters, k=random_password_string_length))

    random_email_with_pw = {'email': email, 'password': random_password}
    logger.debug(f"Randomly generated email and password are :{random_email_with_pw}")

    return random_email_with_pw
