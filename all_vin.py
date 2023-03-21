import os
import pandas

print("""
function:此程序用于拼接指定车辆信息中VIN字符串（以逗号隔开），提高BPG中新增、关联样品效率
input: 规范格式的车辆信息文件路径（例：C:\\Users\\kindr\\Desktop\\Q7报告\\所有车辆信息.xlsx）
author: kindred
time: 2022-8-4
*****************************************************************************""")


xlsx_file = input("输入车辆信息路径：").replace("\"", '').replace('\'', '')
try:
    sheet1 = pandas.read_excel(xlsx_file, index_col=0, sheet_name=0)
    row1, col1 = sheet1.shape

    vin_list = []
    for i in range(row1):
        vin = sheet1.iloc[i, 1]
        vin_list.append(vin)
    vin_str = ','.join(vin_list)
    print(vin_str)
except Exception as e:
    print(e)

os.system('pause')

