import requests

class Request:

    def __init__(self):
        self.session = requests.sessions.session()#实例化一个session
    def request(self,method,url,data=None):
        method = method.upper() #讲字符串转换成大写

        if data is not None and type(data) == str:
            data = eval(data) #讲字符串转换成字典
        print('method:{},url:{}'.format(method,url))
        print('data:{}'.format(data))

        if method == 'GET':
            resp = self.session.request(method,url=url,params=data)
            print('response:{}'.format(resp.text))
            return resp
        elif method == 'POST':
            resp = self.session.request(method,url=url,data=data)
            print('response:{}'.format(resp.text))
            return resp
        else:
            print("错误的请求，请重新输入！")

