import xlwt
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import csv
import time
style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')


datas = [['xingming','nianling'],['xiaoming','122']]

for rowdata in datas:
    # print(rowdata,datas.index(rowdata))
    rowindex = datas.index(rowdata)
    for coldata in rowdata:
        colindex =rowdata.index(coldata)
        print(rowindex,colindex,datas[rowindex][colindex])
        ws.write(rowindex,colindex, datas[rowindex][colindex])
# ws.write(0, 0, 1234.56, style0)
# ws.write(1, 0, datetime.now(), style1)
# ws.write(2, 0, 1)
# ws.write(2, 1, 1)
# ws.write(2, 2, xlwt.Formula("A3+B3"))

wb.save('example.xls')