import unittest
from loan_hanmei.common import doexcel
from loan_hanmei.common.request import Request
from ddt import ddt,data
from loan_hanmei.common import contants

#1.excel里设计第一条用例是正常登录后，充值的时候就可以拿到cookie
#2.用session方式来传递，就需要把request的实例化的对象放到类里
#3.运行用例
@ddt
class RechargeTest(unittest.TestCase):
    cases = doexcel.DoExcel(contants.case_file, "recharge").get_data("recharge")
    request = Request()

    def setUp(self):
        pass
    def tearDown(self):
        pass

    @data(*cases)
    def test_login(self,case):
        print("开始执行第{}个测试用例：".format(case.case_id))
        resp = self.request.request(method=case.method,url = case.url,data=case.data)
        doexcels = doexcel.DoExcel(contants.case_file, "recharge")
        try:
            self.assertEqual(case.expected,resp.text)
            doexcels.write_back(row=case.case_id + 2, col=8, value="PASS", sheet_name="recharge")
        except AssertionError as  e:
            doexcels.write_back(row=case.case_id + 2, col=8, value="FAIlED", sheet_name="recharge")
            raise e
        doexcels.write_back(case.case_id+2,7,resp.text,sheet_name="recharge")
        print(resp.text)