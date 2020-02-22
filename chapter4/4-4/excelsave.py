from openpyxl import Workbook

wb = Workbook()
wb.save('data.xlsx')
print('saved.')