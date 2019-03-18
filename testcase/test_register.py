import unittest
from loan_hanmei.common import doexcel
from loan_hanmei.common.request import Request
from ddt import ddt,data
from loan_hanmei.common.mysql import MysqlUtil
from loan_hanmei.common.config import ReadConfig
from loan_hanmei.common import contants

@ddt
class RegisterTest(unittest.TestCase):
    cases = doexcel.DoExcel(contants.case_file, "reg").get_data("reg")
    request = Request()
    def setUp(self):
        pass
    def tearDown(self):
        pass

    mysql = MysqlUtil()
    sql = "select max(mobilephone) from future.member"
    max = mysql.fetchone(sql)[0]
    @data(*cases)
    def test_reg(self,case):
        print("开始执行第{}个测试用例：".format(case.case_id))
        import json
        data_dict = json.loads(case.data)
        if data_dict["mobilephone"] == "${register_mobile}":
            data_dict["mobilephone"] = int(self.max)+1
        read_config = ReadConfig()
        pre_url = read_config.get("api","pre_url")
        resp = self.request.request(method=case.method,url = pre_url+case.url,data=data_dict)
        doexcels = doexcel.DoExcel(contants.case_file, "reg")
        try:
            self.assertEqual(case.expected,resp.text)
            doexcels.write_back(row=case.case_id + 1, col=8, value="PASS", sheet_name="reg")
        except AssertionError as  e:
            doexcels.write_back(row=case.case_id + 1, col=8, value="FAIlED", sheet_name="reg")
        doexcels.write_back(case.case_id+1,7,resp.text,sheet_name="reg")
        print(resp.text)