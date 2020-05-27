from utils.operation_excel import OperationExcel
from base.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath, parse
from config.config_global import *
import json
from utils.Log import *


# 获取依赖数据
class DependentData(object):
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.data = GetData()
        self.run_method = RunMethod()

    '''通过case_id去获取该case_id的整行数据'''

    def get_case_line_data(self):
        try:
            rows_data = self.opera_excel.get_rows_data(self.case_id)
            return rows_data
        except Exception as e:
            logging.info("错误为：", e)

    '''执行依赖测试，获取结果'''

    def run_dependent(self):
        try:

            row_num = self.opera_excel.get_row_num(self.case_id)

            request_data = self.data.get_data_for_json(row_num)
            header = self.data.is_header(row_num)

            method = self.data.get_request_method(row_num)
            url = self.data.get_request_url(row_num)

            res = self.run_method.run_main(method, url, request_data, header)

            # return res
            return json.loads(res)
        except Exception as e:
            logging.info("错误为：", e)

    '''根据依赖的key去获取执行依赖测试case的响应，
        然后返回,都要为字典格式,所以将上面的run_dependent函数的结果以字典的格式返回'''

    def get_data_for_key(self, row):
        try:
            # rows.[0].productID
            # depend_data是依赖的返回数据 rows.[0].productID
            depend_data = self.data.get_depend_key(row)

            response_data = self.run_dependent()

            json_exe = parse(depend_data)
            madle = json_exe.find(response_data)

            return [math.value for math in madle][0]

        except Exception as e:
            logging.info("错误为：", e)

    dic = {}

    # 把依赖数据保存到文件里
    def save_depend_value(self, res, depend_data, dict_key):

        res = json.loads(res)
        depend_data = list(depend_data.split(","))
        dict_key = list(dict_key.split(","))
        for i in range(len(dict_key)):
            try:
                json_exe = parse(depend_data[i])
                madle = json_exe.find(res)
                value = [math.value for math in madle][0]
                with open(depend_data_path, 'r', encoding='utf-8') as f:
                    depend_value = f.read()
                    if depend_value == "":
                        depend_value = "{}"
                    depend_value = json.loads(depend_value)
                    key = dict_key[i]
                    depend_value[key] = value

            except IndexError as e:
                logging.info("错误为：", e)
            finally:
                try:
                    with open(depend_data_path, 'w', encoding='utf-8') as f:
                        depend_value = json.dump(depend_value, f)

                        f.flush()
                except Exception as e:
                    logging.info("错误为：", e)


#
# res={
#     "total": 2,
#     "rows": [
#         {
#             "productID": "87f8a2e8-8400-4273-834b-762effd51e5e",
#             "productClass": 1,
#             "productName": "88555",
#             "variety": 6,
#             "executiveStandard": 5,
#             "placeOrigin": 4,
#             "featurePoint": "[]",
#             "lastUpdateTime": "2019-05-08 21:58:37"
#         },
#         {
#             "productID": "1182fdab-73f6-4ea4-9714-0fdd0b41eea9",
#             "productClass": 1,
#             "productName": "999",
#             "variety": 1,
#             "executiveStandard": 3,
#             "placeOrigin": 2,
#             "featurePoint": "[]",
#             "lastUpdateTime": "2019-05-08 21:57:44"
#         }
#     ]
# }
# res=json.dumps(res)

if __name__ == '__main__':
    dev = DependentData('login_004')
    dev.save_depend_value(res, ["rows.[0].productID", "rows.[0].productName", "rows.[0].lastUpdateTime"],
                          ["chanpinid", "test", "mode"])
    # logging.info(dev.for_key())
