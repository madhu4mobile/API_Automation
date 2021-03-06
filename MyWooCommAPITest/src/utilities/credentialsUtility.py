import os

class CredentialsUtility(object):

    def __init__(self):
        pass

    @staticmethod
    def get_wc_api_keys():
#----> Using Static Method we dont need to instantiate the object while calling.
        wc_key = os.environ.get('WC_KEY')
        wc_secret = os.environ.get('WC_SECRET')

        if not wc_key or not wc_secret:
            raise Exception("The API credentials 'WC_KEY' and 'WC_SECRET' must be set in env variables")
        else:
            return {'wc_key' : wc_key, 'wc_secret' : wc_secret}
