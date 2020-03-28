# 导包
import unittest
import requests
from api.login_api import LoginApi
from utils import read_login_data
from parameterized import parameterized
from app import BASE_DIR
# 创建测试类
class TestIHRMLogin(unittest.TestCase):

    # 进行初始化
    def setUp(self):
        self.login_api = LoginApi()
    def tearDown(self):
        pass
    # 创建测试函数
    filename = BASE_DIR + "/data/login.json"
    @parameterized.expand(read_login_data(filename))
    def test01_login(self,casename,mobile,password,success,code,message):
        # 使用封装的api登录接口登录
        reque = self.login_api.login(mobile,password)
        # 打印登录结果
        print("登陆的结果",reque.json())
        # 对登录结果进行断言
        # self.assertEqual(success,code,message)
        self.assertEqual(success,reque.json().get("success"))
        self.assertEqual(code,reque.json().get("code"))
        self.assertEqual(message,reque.json().get("message"))