import unittest
from scripts.test_ihrm_login import TestIHRMLogin
from HTMLTestRunner_PY3 import HTMLTestRunner
import time
from app import BASE_DIR
# 创建测试套件
suite = unittest.TestSuite()
# 添加测试用例到测试套件
suite.addTest(unittest.makeSuite(TestIHRMLogin))
# 使用runner来运行测试套件
# 定义测试报告的文件名称
# reportname = BASE_DIR + "/report/report {}.html".format(time.strftime("%Y%m%d %H%M%S"))
reportname = BASE_DIR + "/report/report.html"
with open(reportname,'wb') as f:
    runner = HTMLTestRunner(f,verbosity=2,description="这是测试报告",title="IHRM报告")
    runner.run(suite)