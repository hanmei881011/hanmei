import requests
from loan_hanmei.common import doexcel
from loan_hanmei.testcase.login_test import laon
from loan_hanmei.common.request import Request

#充值接口
cases=doexcel.DoExcel("..//datas/loantest.xlsx","recharge").get_data("recharge")
class Recharge:
    def recharge(self):
        for case  in cases:
            # data1 = eval(case.data)
            # session = session.session()
            request = Request()
            resp = request.request(method=case.method,url = case.url,data=case.data)
            doexcels = doexcel.DoExcel("..//datas/loantest.xlsx", "recharge")
            if case.expected == resp.text:
                doexcels.write_back(row=case.case_id + 1, col=8, value="PASS",sheet_name="recharge")
            else:
                doexcels.write_back(row=case.case_id + 1, col=8, value="FAIlED",sheet_name="recharge")
            # doexcels.write_back(case.case_id+1,6,resp.text,sheet_name="recharge")
            print(resp.text)
#
recharge=Recharge()
recharge.recharge()
