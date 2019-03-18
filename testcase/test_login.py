import unittest
from loan_hanmei.common import doexcel
from loan_hanmei.common.request import Request
from ddt import ddt,data
# from loan_hanmei.common.logger import get_logger
from loan_hanmei.common import logger
from loan_hanmei.common import contants

logg = logger.get_logger("login_test")
@ddt
class LoginTest(unittest.TestCase):
    cases = doexcel.DoExcel(contants.case_file, "login").get_data("login")
    request = Request()
    def setUp(self):
        pass
    def tearDown(self):
        pass

    @data(*cases)
    def test_login(self,case):
        logg.info("开始执行第{}个测试用例：".format(case.case_id))
        resp = self.request.request(method=case.method,url = case.url,data=case.data)
        doexcels = doexcel.DoExcel(contants.case_file, "login")
        try:
            self.assertEqual(case.expected,resp.text)
            doexcels.write_back(row=case.case_id + 1, col=8, value="PASS", sheet_name="login")
        except AssertionError as  e:
            doexcels.write_back(row=case.case_id + 1, col=8, value="FAIlED", sheet_name="login")
            logg.error("第{}个用例执行结果：failed".format(case.case_id))
        doexcels.write_back(case.case_id+1,7,resp.text,sheet_name="login")
        logg.info(resp.text)