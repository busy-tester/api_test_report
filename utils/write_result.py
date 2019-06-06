from utils.Log import *
from utils.operation_excel import OperationExcel
from config.config_global import *
from data.data_config import *
from utils.Excel_Obj import *


def writeTestResult(sheetObj, rowNo, testResult, errorInfo=None, picPath=None):
    colorDict = {"pass": "green", "faild": "red", "": None, "skip": "yellow"}


    try:

        excelObj.write_value(sheetObj, content=testResult, rowNo=rowNo, colsNo=get_result(),
                             style=colorDict[testResult])
        if testResult == "":
            # 清空时间单元格
            excelObj.write_value(sheetObj, content='', rowNo=rowNo, colsNo=get_run_time())
            excelObj.write_value(sheetObj, content='', rowNo=rowNo, colsNo=get_error_msg())
        else:
            excelObj.writeCellCurrentTime(sheetObj, rowNo=rowNo, colsNo=get_run_time())
            excelObj.write_value(sheetObj, content=errorInfo, rowNo=rowNo, colsNo=get_error_msg())

    except Exception as e:
        logging.info('写excel时发生错误')
        # logging.info(traceback.logging.info_exc())
