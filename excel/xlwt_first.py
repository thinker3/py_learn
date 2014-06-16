from xlwt import Workbook

wb = Workbook()
ws = wb.add_sheet('numbers')
for i in xrange(10):
    for j in xrange(10):
        ws.write(i, j, i*j)

ws = wb.add_sheet('letters')
for i in xrange(5):
    for j in xrange(5):
        ws.write(i, j, 'a')
wb.save('First.xls')
