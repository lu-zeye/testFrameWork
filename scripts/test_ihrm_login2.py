import unittest
import requests
from api.login_api2 import LoginApi
from utils2 import read_login_data
from parameterized import parameterized
from app import BASE_DIR

class TestIHRMLogin(unittest.TestCase):
    def setUp(self):
        self.login_api = LoginApi()
    def tearDown(self):
        pass
    filename = BASE_DIR + "/data/login2.json"
    @parameterized.expand(read_login_data(filename))
    def test01_login(self,name,mobile,password,seccess,code):
        reque = self.login_api.login(mobile,password)
        print(reque.json())
        self.assertEqual(seccess,reque.json().get("success"))
        self.assertEqual(code,reque.json().get("code"))