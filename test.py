import pandas as pd

path = r"C:\Users\kindred\Desktop\所有车辆信息.xlsx"
sheet1 = pd.read_excel(path, sheet_name=0, index_col=0)
rows, cols = sheet1.shape

value = sheet1.iloc[15, 7]
# .strftime('%Y-%m')
print(value)
print(type(value))

