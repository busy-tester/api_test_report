from utils.Log import *
from utils.operation_excel import OperationExcel
from config.config_global import *
from data.data_config import *
from utils.Excel_Obj import *

#往Excel中写入测试结果信息的公共方法



#用例或用例步骤执行结束后，向Excel中写执行结果信息
def writeTestResult(sheetObj, rowNo, testResult, errorInfo=None, picPath=None):
    # 测试通过结果信息为绿色，失败为红色
    colorDict = {"pass": "green", "faild": "red", "": None, "skip": "yellow"}
    # colsDict={
    #     "testCase":[testCase_runTime,testCase_testResult],
    #     "caseStep":[testStep_runTime,testStep_testResult],
    #     "dataSheet":[dataSource_runTime,dataSource_result]
    # }

    try:
        # 在测试步骤sheet中，写入测试结果,testResult为pass或faild
        excelObj.write_value(sheetObj, content=testResult, rowNo=rowNo, colsNo=get_result(),
                             style=colorDict[testResult])
        if testResult == "":
            # 清空时间单元格
            excelObj.write_value(sheetObj, content='', rowNo=rowNo, colsNo=get_run_time())
            # 清空错误信息单元格
            excelObj.write_value(sheetObj, content='', rowNo=rowNo, colsNo=get_error_msg())
        else:
            # 在测试步骤sheet中，写入测试时间
            excelObj.writeCellCurrentTime(sheetObj, rowNo=rowNo, colsNo=get_run_time())
            # 在测试步骤sheet中，写入异常信息
            excelObj.write_value(sheetObj, content=errorInfo, rowNo=rowNo, colsNo=get_error_msg())

    except Exception as e:
        logging.info('写excel时发生错误')
        # logging.info(traceback.logging.info_exc())
