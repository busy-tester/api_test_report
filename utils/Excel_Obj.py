from utils.operation_excel import OperationExcel
from config.config_global import *

#创建解析Excel对象
excelObj=OperationExcel()

#将Excel数据文件加载到内存
excelObj.loadWorkBook(excelpath)