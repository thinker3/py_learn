#coding=utf8
from xlwt import Workbook

class Person():
    pass

obj = Person()
obj.name = 'chenkun'
obj.age = 27
obj.height = 163
obj.weight = 60

book = Workbook()
sheet = book.add_sheet('columns')

columns = [
        ['name', u'姓名', 8],
        ['age', u'年龄', 6],
        ['height', u'身高', 6],
        ['weight', u'体重', 6],
    ]
def index_of(key, list_2d):
    for i, one in enumerate(list_2d):
        if key == one[0]:
            return i

for i in xrange(len(columns)):
    sheet.write(0, i, columns[i][1]) 
    sheet.col(i).width = columns[i][2] * 256
for i in xrange(1, 10):
    sheet.write(i, index_of('name', columns), obj.name)
    sheet.write(i, index_of('age', columns), obj.age)
    sheet.write(i, index_of('height', columns), obj.height)
    sheet.write(i, index_of('weight', columns), obj.weight)

book.save('Columns.xls')
