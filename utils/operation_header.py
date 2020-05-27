from base.runmethod import RunMethod
from utils.Log import *


class OPerationHeader(object):
    def __init__(self, res, method, url, data):
        self.res = res
        self.method = method
        self.url = url
        self.data = data
        self.run_method = RunMethod()

    def write_cookie(self):
        with open('../data_file/cookie.json', 'w') as f:
            res = self.run_method.run_main(self.method, self.url, self.data)
            cookie = res.cookies
            f.write(cookie)

    def get_data(self):
        pass

        # 写入cookie
        # if header=='w':
        #     res = self.run_method.run_main(method, url,data)
        #     logging.info('res====',res)
        #     op_header=OPerationHeader(res,method,url,data)
        #     op_header.write_cookie()
        #
        # elif header=='y':
        #     op_json=OperationJson('../data_file/cookie.json')
        #     cookie=op_header.get_data()
        #     res = self.run_method.run_main(method, url, data, cookie)
        #
        # else:
        #     res = self.run_method.run_main(method, url, data, header)
