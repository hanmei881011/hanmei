import unittest
from common import doexcel
from common.request import Request
from ddt import ddt,data
from common.config import ReadConfig
from common import contants


@ddt
class AddloanTest(unittest.TestCase):
    cases = doexcel.DoExcel(contants.case_file, "addloan").get_data("addloan")
    request = Request()
    def setUp(self):
        pass
    def tearDown(self):
        pass

    @data(*cases)
    def test_addloan(self,case):
        readconfig = ReadConfig()
        pre_url = readconfig.get("api","pre_url")
        print("开始执行第{}个测试用例：".format(case.case_id))
        resp = self.request.request(method=case.method,url = pre_url+case.url,data=case.data)
        doexcels = doexcel.DoExcel(contants.case_file, "addloan")
        try:
            self.assertEqual(case.expected,resp.text)
            doexcels.write_back(row=case.case_id + 2, col=8, value="PASS", sheet_name="addloan")
        except AssertionError as  e:
            doexcels.write_back(row=case.case_id + 2, col=8, value="FAIlED", sheet_name="addloan")
        doexcels.write_back(case.case_id + 2,7,resp.text,sheet_name="addloan")
        print(resp.text)