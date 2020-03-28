import unittest
from scripts.test_ihrm_login import TestIHRMLogin
from HTMLTestRunner_PY3 import HTMLTestRunner
import time
from app import BASE_DIR

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestIHRMLogin))

reportname = BASE_DIR + "/report/report.html"
with open(reportname,'wb') as f:
    runner = HTMLTestRunner(f,verbosity=2,description="测试报告",title="IHRM报告")
    runner.run(suite)