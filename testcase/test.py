import requests
session = requests.session()
data1 = {"mobilephone":"18800000001","pwd":"123456"}
data2 = {"mobilephone":"18800000001","amount":""}
resp1 = session.request("post",url="http://47.107.168.87:8080/futureloan/mvc/api/member/login",data=data1)
resp2 = session.request("post",url="http://47.107.168.87:8080/futureloan/mvc/api/member/recharge",data=data2)
print("返回结果：",resp2.text)


#case.py ---测试用例
#suit.py ---测试套件
#loader.py ---加载测试用例
#run.py ---执行测试用例
#result.py ---测试结果，测试报告
#main
#mock ---模拟测试（数据）