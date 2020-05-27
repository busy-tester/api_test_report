from main.run_test import TestRun
import ddt
import unittest
import sys
import HTMLTestRunner

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

obj = OperationExcel()
all_data = obj.get_excel_all_data()
@ddt.ddt
class TestAllCase(unittest.TestCase):
    def setUp(self):
        self.run = TestRun()
        self.data = GetData()
        self.run_method = RunMethod()
        self.common_util = CommonUtil()
        self.send_email = SendEmail()
        self.excel = OperationExcel()
        self.sheet_obj = self.excel.get_data()


    @ddt.data(*all_data)
    def test_all_case(self, data):  # 提取值 提取值的key 待替换的key 实际替换的key
        get_num, get_case_des, get_api, get_exec, get_module, get_pre, get_url, get_header, get_method, get_parames, get_hope_http_code, get_hope_response, get_results, get_run_time, get_error_msg, get_depend_Value, get_setting_key, get_wait_key, get_actual_key = data
        print(get_num, get_case_des, get_api, get_exec, get_module, get_pre, get_url, get_header, get_method, get_parames, get_hope_http_code, get_hope_response, get_results, get_run_time, get_error_msg, get_depend_Value, get_setting_key, get_wait_key, get_actual_key)
        print("="*20)
        print(*all_data)

        # run.test_run()
        res = None
        pass_count = []
        fail_count = []
        skip_count = []

        run_num = [2, 1]

        is_run = get_exec  # exec

        message = get_case_des

        api_name = get_api
        if is_run == 'y':

            url_path = get_url

            url = config_global.base_url[0] + url_path

            method = get_method

            data = get_parames

            code = get_hope_http_code

            expect = get_hope_response

            headers = get_header

            depend_Value = get_depend_Value  # tiquzhi

            set_key = get_setting_key

            wait_key = get_wait_key

            actual_key = get_actual_key

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

            # depend_case = data.is_depend(num)
            depend_case = get_num
            #
            # if depend_case != None:
            #     self.depend_data = DependentData(depend_case)
            #     # 获取的依赖响应
            #     depend_response_data = self.depend_data.get_data_for_key(i)
            #
            #     # 获取依赖的key
            #     depend_key = self.data.get_depend_field(i)
            #
            #     # 更新参数值
            #     data[depend_key] = depend_response_data
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
                        self.assertTrue(True)  # 断言
                        writeTestResult(excelObj.get_data(), rowNo=get_num, testResult='pass')
                        pass_count.append(get_num)

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

                        writeTestResult(excelObj.get_data(), rowNo=get_num, testResult='faild', errorInfo=res)
                        self.assertTrue(False, msg=res)  # 断言

                        fail_count.append(get_num)


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

                    writeTestResult(excelObj.get_data(), rowNo=get_num, testResult='faild', errorInfo=res)
                    fail_count.append(get_num)

            fail_run()
        else:
            logging.info('%s接口:%s->接口不执行' % (api_name, message))
            skip_count.append(get_num)
            writeTestResult(excelObj.get_data(), rowNo=get_num, testResult='skip')

# 发送邮件
# logging.info("正在发送邮件，请等待。。。")
# send_email.send_main(pass_count,fail_count,skip_count)


if __name__ == '__main__':
    # unittest.main()
    # # 发送邮件
    # logging.info("正在发送邮件，请等待。。。")

    with open(report_path, 'wb') as f:
        # 第一个参数，文件路径，第二个参数，匹配规则
        suite = unittest.defaultTestLoader.discover(case_path, pattern='test*.py')
        # unittest.TextTestRunner().run(suite)
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=0, title='api测试报告', description='描述')
        runner.run(suite)
