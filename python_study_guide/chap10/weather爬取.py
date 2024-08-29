import weather
import openpyxl
html=weather.get_html()  # 发请求，得响应结果
lst=weather.parse_html(html)   # 解析数据
# 创建一个想你的excel工作簿

workbook=openpyxl.Workbook() # 创始对象
# 在excel中创建工作表

sheet=workbook.create_sheet('景区天气')
# 向工作表中添加数据
for item in lst:
    sheet.append(item)


workbook.save('weather.xlsx')





