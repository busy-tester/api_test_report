import time
from utils.Log import *
from config.config_global import *


# 获取当前时间
def nowTime():
    now = int(time.time())
    timeArray = time.localtime(now)
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return currentTime


# 获取手机号
def mobile():
    time_stamp = str(time.time())
    phone = phone_num + time_stamp.split('.')[0][2:]
    return phone


def str_for_list(str_one):
    try:
        # flag = None

        wait_key = str(str_one)
        key_list = wait_key.split(',')
        return key_list

    except Exception as e:
        logging.info("错误为：", e)
