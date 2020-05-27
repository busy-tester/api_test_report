from utils.Log import *

'''断言多个字符串是否在返回值里'''


class CommonUtil(object):
    '''判断字符串str_one在不在字符串str_two中'''

    def is_contain(self, str_one, str_two):

        try:
            flag = None

            '''将str_one转为字符串'''
            str_one = str(str_one)

            # 将获取到的预期结果按,分隔成列表
            str_list = str_one.split(',')

            '''循环列表，判断每一个值是不是在str_two里，全部通过返回True，有一个失败返回False'''

            for n in range(len(str_list)):
                str_one = str_list[n]

                if str_one in str_two:
                    flag = True
                else:
                    return False
            return flag
        except Exception as e:

            logging.info("错误为：", e)
