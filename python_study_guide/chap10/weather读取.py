import openpyxl
# 打开工作簿
workbook=openpyxl.load_workbook('weather.xlsx')
# 选择要操作的工作表
sheet = workbook['景区天气']
# 表格数据是二维列表，先遍历的是行，后遍历是列
lst = [] # 行数据
for row in sheet.rows:
    sub_lst = []  # 单元格数据
    for cell in row:   # cell单元格
        sub_lst.append(cell.value)
    lst.append(sub_lst)

for item in lst:
    print(item)

