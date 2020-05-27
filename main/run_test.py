import sys

sys.path.append(r"F:\api_framework")
from base.runmethod import RunMethod
from data.get_data import GetData
from base.common_method import *
import json
import time
import requests
from utils.commonutil import CommonUtil
from data.dependent_data import DependentData
from utils.send_email import SendEmail
from utils.operation_json import OperationJson
from utils.operation_header import OPerationHeader
from utils.write_result import *
from utils.operation_excel import OperationExcel
from utils.Excel_Obj import *
from utils.Log import *
from config import config_global


class TestRun(object):
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.common_util = CommonUtil()
        self.send_email = SendEmail()
        self.excel = OperationExcel()
        self.sheet_obj = self.excel.get_data()

    def test_run(self):

        res = None
        pass_count = []
        fail_count = []
        skip_count = []
        # 获取多少行
        rows_count = self.data.get_case_lines()

        for i in range(2, rows_count + 1):
            run_num = [2, 1]
            is_run = self.data.get_is_run(i)
            message = self.data.get_api_msg(i)
            api_name = self.data.get_api_name(i)
            if is_run:

                url_path = self.data.get_request_url(i)

                url = config_global.base_url[0] + url_path

                method = self.data.get_request_method(i)

                data = self.data.get_request_data(i)

                code = self.data.get_http_code_data(i)

                expect = self.data.get_expect_data(i)

                headers = self.data.get_request_headers(i)

                depend_Value = self.data.get_depend_value(i)  # tiquzhi

                set_key = self.data.get_set_key(i)

                wait_key = self.data.get_waiting_replace_key(i)

                actual_key = self.data.get_actual_replace_key(i)

                header = get_header_value()

                if data != None:
                    if '88888888' in data:
                        data = data.replace("88888888", "17154654546")
                    data = json.loads(data)

                if headers != None:
                    try:
                        with open(depend_data_path, 'r', encoding='utf-8') as f:
                            header_value = json.load(f)
                            header[headers] = header_value["token"]

                    except Exception as e:
                        logging.info("错误为：", e)

                depend_case = self.data.is_depend(i)

                if depend_case != None:
                    self.depend_data = DependentData(depend_case)
                    # 获取的依赖响应
                    depend_response_data = self.depend_data.get_data_for_key(i)

                    # 获取依赖的key
                    depend_key = self.data.get_depend_field(i)

                    # 更新参数值
                    data[depend_key] = depend_response_data
                '''待提取的key'''
                if wait_key != None:

                    try:
                        with open(depend_data_path, 'r', encoding='utf-8') as f:

                            dependvalue = f.read()

                            depend_value_dict = json.loads(dependvalue)

                        wait_key_list = str_for_list(wait_key)
                        actual_key_list = str_for_list(actual_key)

                        for index_num in range(len(wait_key_list)):
                            Wait_key = wait_key_list[index_num]
                            Act_key = actual_key_list[index_num]
                            depend_value_key = depend_value_dict[Act_key]
                            data[Wait_key] = depend_value_key

                    except Exception as e:
                        logging.info("错误为：", e)

                def fail_run():
                    response = self.run_method.run_main(method, url, data, header)
                    res = response[0]
                    # print('response---->',response)
                    # print('res---->',res)
                    global http_code
                    http_code = response[1]

                    # print(type(http_code), http_code)

                    # 断言

                    if int(code) == http_code:

                        if self.common_util.is_contain(expect, res):
                            logging.info('\033[1;32;m%s接口:%s->接口执行通过\033[0m' % (api_name, message))
                            writeTestResult(excelObj.get_data(), rowNo=i, testResult='pass')
                            pass_count.append(i)

                            if depend_Value != None:
                                self.depend_data = DependentData(depend_case)
                                self.depend_data.save_depend_value(res, depend_Value, set_key)


                        else:
                            fail = run_num[0]
                            fail -= 1
                            run_num[0] = fail

                            while run_num[0]:
                                fail_num = run_num[1]
                                run_num[1] = run_num[1] + 1
                                print('第%s次执行失败，开始第%s次执行。。。' % (fail_num, fail_num + 1))

                                time.sleep(1)
                                logging.info("\033[0;43;41m%s接口:%s->接口执行失败\033[0m" % (api_name, message))

                                fail_run()

                            writeTestResult(excelObj.get_data(), rowNo=i, testResult='faild', errorInfo=res)
                            fail_count.append(i)


                    else:
                        fail = run_num[0]
                        fail -= 1
                        run_num[0] = fail

                        while run_num[0]:
                            fail_num = run_num[1]
                            run_num[1] = run_num[1] + 1

                            print('第%s次执行失败，开始第%s次执行。。。' % (fail_num, fail_num + 1))

                            time.sleep(1)
                            logging.info("\033[0;43;41m%s->接口执行失败\033[0m" % message)

                            fail_run()

                        writeTestResult(excelObj.get_data(), rowNo=i, testResult='faild', errorInfo=res)
                        fail_count.append(i)

                fail_run()
            else:
                logging.info('%s接口:%s->接口不执行' % (api_name, message))
                skip_count.append(i)
                writeTestResult(excelObj.get_data(), rowNo=i, testResult='skip')

            # 发送邮件
        logging.info("正在发送邮件，请等待。。。")
        # self.send_email.send_main(pass_count,fail_count,skip_count)


if __name__ == '__main__':
    # run = RuTest()
    # run.test_run()
    pass
