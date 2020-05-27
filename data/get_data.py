from utils.operation_excel import OperationExcel
from data.data_config import *
from utils.operation_json import OperationJson
from utils.Log import *
import json

'''获取excel里的数据'''


class GetData(object):

    def __init__(self):
        self.opera_excel = OperationExcel()
        self.sheet = self.opera_excel.get_data()

    '''获取excel的行数，就是我们的case个数'''

    def get_case_lines(self):
        try:
            return self.opera_excel.get_lines()
        except Exception as e:
            logging.info("错误为：", e)

    '''获取是否执行'''

    def get_is_run(self, row):
        try:
            flag = None
            col = get_run()
            run_model = self.opera_excel.get_cell_value(row, col)
            if run_model == 'y':
                flag = True
            else:
                flag = False
            return flag
        except Exception as e:
            logging.info("错误为：", e)

    '''获取接口描述'''

    def get_api_msg(self, row):
        try:
            col = get_request_name()
            api_msg = self.opera_excel.get_cell_value(row, col)
            return api_msg
        except Exception as e:
            logging.info("错误为：", e)

    '''获取接口名称'''

    def get_api_name(self, row):
        try:
            col = get_api_name()
            api_name = self.opera_excel.get_cell_value(row, col)
            return api_name
        except Exception as e:
            logging.info("错误为：", e)

    '''是否携带header'''

    def get_request_headers(self, row):
        try:
            col = get_header()
            header = self.opera_excel.get_cell_value(row, col)
            if header == '':
                return None
            return header
        except Exception as e:
            logging.info("错误为：", e)

    '''是否有header'''

    def is_header(self, row):
        try:
            col = get_header()
            header = self.opera_excel.get_cell_value(row, col)

            if header != 'n':
                header = json.loads(header)
                return header
                # return self.opera_excel.get_cell_value(row,col)
            elif header == 'w':
                return 'w'
            else:
                return None
        except Exception as e:
            logging.info("错误为：", e)

    '''获取请求方式'''

    def get_request_method(self, row):
        try:
            col = get_run_way()
            request_method = self.opera_excel.get_cell_value(row, col)
            return request_method
        except Exception as e:
            logging.info("错误为：", e)

    '''获取url'''

    def get_request_url(self, row):
        try:
            col = get_url()
            url = self.opera_excel.get_cell_value(row, col)
            return url
        except Exception as e:
            logging.info("错误为：", e)

    '''请求数据'''

    def get_request_data(self, row):
        try:
            col = get_data()
            data = self.opera_excel.get_cell_value(row, col)
            if data == '':
                return None
            return data
        except Exception as e:
            logging.info("错误为：", e)

    '''通过获取关键字拿到data数据'''

    def get_data_for_json(self, row):
        try:
            opera_json = OperationJson()
            request_data = opera_json.get_data(self.get_request_data(row))
            return request_data
        except Exception as e:
            logging.info("错误为：", e)

    '''获取要提取的字段的值'''

    def get_depend_value(self, row):
        try:
            col = get_depend_value()
            depend_value = self.opera_excel.get_cell_value(row, col)
            if depend_value == '':
                return None
            return depend_value
        except Exception as e:
            logging.info("错误为：", e)

    '''获取预期结果'''

    def get_expect_data(self, row):
        try:
            col = get_expect()
            expect = self.opera_excel.get_cell_value(row, col)
            if expect == '':
                return None
            return expect
        except Exception as e:
            logging.info("错误为：", e)

    '''获取http状态码'''

    def get_http_code_data(self, row):
        try:
            col = get_http_code()
            http_code = self.opera_excel.get_cell_value(row, col)
            return http_code
        except Exception as e:
            logging.info("错误为：", e)

    '''获取待替换的值'''

    def get_waiting_replace_key(self, row):
        try:
            col = get_waiting_replace_key()
            wait_rep_key = self.opera_excel.get_cell_value(row, col)
            if wait_rep_key == '':
                return None
            return wait_rep_key
        except Exception as e:
            logging.info('错误为：', e)

    '''获取实际替换的值'''

    def get_actual_replace_key(self, row):
        try:
            col = get_actual_replace_key()
            act_rep_key = self.opera_excel.get_cell_value(row, col)
            if act_rep_key == '':
                return None
            return act_rep_key
        except Exception as e:
            logging.info('错误为：', e)

    '''写入数据'''

    def write_result(self, row, value):
        try:
            col = get_result()
            self.opera_excel.write_value(sheet=self.sheet, content=value, rowNo=row, colsNo=col)
        except Exception as e:
            logging.info("错误为：", e)

    '''获取依赖返回数据的key'''

    def get_depend_key(self, row):
        try:
            col = get_data_depend()
            depent_key = self.opera_excel.get_cell_value(row, col)
            if depent_key == "":
                return None
            else:
                return depent_key
        except Exception as e:
            logging.info("错误为：", e)

    def is_depend(self, row):  # 是否有依赖
        try:
            col = get_case_depend()
            depend_case_id = self.opera_excel.get_cell_value(row, col)
            if depend_case_id == "":
                return None
            else:
                return depend_case_id
        except Exception as e:
            logging.info("错误为：", e)

    '''获取数据依赖字段'''

    def get_depend_field(self, row):
        try:
            col = get_field_depend()
            data = self.opera_excel.get_cell_value(row, col)
            if data == "":
                return None
            else:
                return data
        except Exception as e:
            logging.info("错误为：", e)

    '''获取请求方式'''

    def get_set_key(self, row):
        try:
            col = get_set_key()
            request_method = self.opera_excel.get_cell_value(row, col)
            return request_method
        except Exception as e:
            logging.info("错误为：", e)
