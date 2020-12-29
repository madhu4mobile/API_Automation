
import requests
import os
from MyWooCommAPITest.src.configs.hosts_Configs import API_HOSTS
from requests_oauthlib import OAuth1
import json


class requestUtility(object):

    def __init__(self):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1("ck_a29265ef5bc096bd7cec4266a7732ff63463521a","cs_4ac296939dcd86e2aef8b541b9f1c2ad8582a93b")

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
