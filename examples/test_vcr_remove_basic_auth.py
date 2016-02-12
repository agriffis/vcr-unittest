from vcr_unittest import VCRTestCase
import requests
"""
This example shows how you can use the private _get_vcr_kwargs to pass through
keyword arguments to vcr.

For more information on filtering
"""
class MyTestCase(VCRTestCase):
    def _get_vcr_kwargs(self):
        """This removes the authorization header from VCR so we don't record your auth parameters"""
        return {
            'filter_headers': ['Authorization']
        }

    def test_no_basic_auth_in_cassette(self):
        response = requests.get('http://example.com', auth=HTTPBasicAuth('user', 'pass'))
