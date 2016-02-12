from mylib import MyClient
from vcr_unittest import VCRTestCase

"""
This is an example test case showing that if you define your own
setUp method, you will need to run setUp for the VCRTestCase class
as well
"""

class MyClientTestCase(VCRTestCase):
    def setUp(self):
        super(MyClientTestCase, self).setUp()
        self.client = MyClient('user', 'pass')

    def test_my_api_call(self):
        self.my_api_call()
