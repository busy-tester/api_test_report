import requests
import json

import urllib3

requests.packages.urllib3.disable_warnings()
s = requests.Session()
from utils.Log import *


class RunMethod(object):
    def __init__(self):
        self.s = requests.Session()

    def post_main(self, url, data, header=None):
        try:
            res = None
            if header != None:
                http_code = s.post(url=url, json=data, timeout=10, headers=header, verify=False)
                res=http_code.json()

            else:
                http_code = s.post(url=url, json=data, timeout=10, verify=False)
                res = http_code.json()

            return res, http_code.status_code
        except Exception as e:
            logging.info("错误为：", e)

    def get_main(self, url, data=None, header=None):

        try:
            res = None
            if header != None:
                http_code = s.get(url=url, json=data, headers=header, timeout=10, verify=False)
                res = http_code.json()
            else:
                http_code = s.get(url=url, json=data, timeout=10, verify=False)
                res = http_code.json()
            return res, http_code.status_code
            # return res.text
        except Exception as e:
            logging.info("错误为：", e)

    def run_main(self, method, url, data=None, header=None):
        try:
            res = None
            if method == 'post':
                res = self.post_main(url, data, header)
                code = res[1]
                resp = res[0]


            else:
                res = self.get_main(url, data, header)
                code = res[1]
                resp = res[0]
            return json.dumps(resp, ensure_ascii=False, sort_keys=True, indent=2), code
        except Exception as e:
            logging.info("错误为：", e)
