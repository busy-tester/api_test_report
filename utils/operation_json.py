import json
from config.config_global import *
from utils.Log import *


class OperationJson(object):

    def __init__(self, file_path=None):

        if file_path == None:
            self.file_path = json_file_path

        else:
            self.file_path = file_path

        self.data = self.read_data()

    '''读取json文件'''

    def read_data(self):
        try:
            with open(self.file_path) as fp:
                data = json.load(fp)
                return data
        except Exception as e:
            logging.info("错误为：", e)

    # def get_data(self,id):
    #     return self.data[id]
    '''根据关键字获取数据'''

    def get_data(self, id):
        try:
            if id == None:
                return None
            return self.data[id]
        except Exception as e:
            logging.info("错误为：", e)

    '''写入cookies'''

    def write_data(self, data):
        with open(json_file_path, 'w') as fp:
            fp.write(json.dumps(data))


if __name__ == '__main__':
    opejson = OperationJson()
    logging.info(opejson.get_data('login_001'))
