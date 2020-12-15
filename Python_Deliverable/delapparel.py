import openpyxl

wb = openpyxl.load_workbook('rawintake.xlsx')
ws1 = wb.active

for x in range(0, 50):
    for row in ws1:
        for cell in row:
            if cell.value == "MENS APPAREL" or cell.value == "LADIES APPAREL" or cell.value == "CHILDRENS APPAREL":
                ws1.delete_rows(cell.row)
wb.save("rawintake.xlsx")
print('done')