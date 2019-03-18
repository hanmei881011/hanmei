import requests
from loan_hanmei.common import doexcel
from loan_hanmei.common.request import Request

#注册接口
# data = {'mobilephone':'18800000001',"pwd":"123456","regname":"妖孽"}
# resp = requests.post("http://47.107.168.87:8080/futureloan/mvc/api/member/register",data=data)
# print('响应信息', resp.text)

#登录接口 post ---表单传参 ---

cases=doexcel.DoExcel("..//datas/loantest.xlsx","login").get_data("login")
class laon:
    def login(self):
        for case  in cases:
            # data1 = eval(case.data)
            # session = requests.session()

            request = Request()
            resp = request.request(method=case.method,url = case.url,data=case.data)
            # print('响应信息', resp1.text)
            doexcels = doexcel.DoExcel("..//datas/loantest.xlsx", "login")
            if case.expected == resp.text:
                doexcels.write_back(row=case.case_id + 1, col=8, value="PASS",sheet_name="login")
            else:
                doexcels.write_back(row=case.case_id + 1, col=8, value="FAIlED",sheet_name="login")
            doexcels.write_back(case.case_id+1,6,resp.text,sheet_name="login")
            print(resp.text)
#
laon=laon()
laon.login()





