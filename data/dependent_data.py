from utils.operation_excel import OperationExcel
from base.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath, parse
from config.config_global import *
import json
from utils.Log import *


class DependentData(object):
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.data = GetData()
        self.run_method = RunMethod()

    def get_case_line_data(self):
        try:
            rows_data = self.opera_excel.get_rows_data(self.case_id)
            return rows_data
        except Exception as e:
            logging.info("错误为：", e)

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

    def get_data_for_key(self, row):
        try:
            # rows.[0].productID
            depend_data = self.data.get_depend_key(row)

            response_data = self.run_dependent()

            json_exe = parse(depend_data)
            madle = json_exe.find(response_data)

            return [math.value for math in madle][0]

        except Exception as e:
            logging.info("错误为：", e)

    dic = {}

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
# if __name__ == '__main__':
#     dev = DependentData('login_004')
#     dev.save_depend_value(res, ["rows.[0].productID", "rows.[0].productName", "rows.[0].lastUpdateTime"],
#                           ["chanpinid", "test", "mode"])
#     # logging.info(dev.for_key())
