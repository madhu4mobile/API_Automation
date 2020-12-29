
import requests
import os
from MyWooCommAPITest.src.configs.hosts_Configs import API_HOSTS
from requests_oauthlib import OAuth1
from MyWooCommAPITest.src.utilities.credentialsUtility import CredentialsUtility
import json


class requestUtility(object):

    def __init__(self):
        wc_creds = CredentialsUtility.get_wc_api_keys() # could be directly called becuase of @staticmethod
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        import pdb; pdb.set_trace()
        self.auth = OAuth1(wc_creds['wc_key'],wc_creds['wc_secret'])

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        myURL = self.base_url + endpoint
        req_api = requests.post(url=myURL, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = req_api.status_code
        assert self.status_code == int(expected_status_code),\
        f'Expected status code {expected_status_code} but actual {self.status_code}'
                # while breaking a line use skip character '\'
        #import pdb; pdb.set_trace()

        return req_api.json()

    def get(self):
        pass
