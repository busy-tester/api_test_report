from utils.Log import *


class CommonUtil(object):

    def is_contain(self, str_one, str_two):

        try:
            flag = None

            '''将str_one转为字符串'''
            str_one = str(str_one)
            str_list = str_one.split(',')

            for n in range(len(str_list)):
                str_one = str_list[n]

                if str_one in str_two:
                    flag = True
                else:
                    return False
            return flag
        except Exception as e:

            logging.info("错误为：", e)