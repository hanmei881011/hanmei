import unittest
from common import doexcel
from common.request import Request
from ddt import ddt,data
from common.config import ReadConfig
from common.context import replace
from common.context import Context
from common.mysql import MysqlUtil
from common import contants

@ddt
class InvestTest(unittest.TestCase):
    cases = doexcel.DoExcel(contants.case_file, "invest").get_data("invest")
    request = Request()
    @classmethod
    def setUpClass(cls):
        cls.mysql = MysqlUtil()
    @classmethod
    def tearDownClass(cls):
        cls.mysql.close()

    @data(*cases)
    def test_invest(self,case):
        readconfig = ReadConfig()
        pre_url = readconfig.get("api","pre_url")
        print("开始执行第{}个测试用例：".format(case.case_id))
        case.data = replace(case.data)
        resp = self.request.request(method=case.method,url = pre_url+case.url,data=case.data)
        doexcels = doexcel.DoExcel(contants.case_file, "invest")
        try:
            self.assertEqual(case.expected,resp.text)
            doexcels.write_back(row=case.case_id + 2, col=8, value="PASS", sheet_name="invest")
            #加一层判断，判断加标是否成功，如果成功，就把标的的ID查出来反射给类的属性，以便下一条用例取
            if resp.json()["msg"] == "加标成功":
                load_member_id = getattr(Context,"loan_member_id")
                mysql = MysqlUtil()
                sql = "select Id from future.loan where MemberID={} order by CreateTime desc limit 1".format(load_member_id)
                loan_id = mysql.fetchone(sql)[0]
                setattr(Context,"loan_id",str(loan_id))
        except AssertionError as  e:
            doexcels.write_back(row=case.case_id + 2, col=8, value="FAIlED", sheet_name="invest")
        doexcels.write_back(case.case_id + 2,7,resp.text,sheet_name="invest")
        print(resp.text)