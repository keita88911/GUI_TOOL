#coding=utf-8

import xlrd
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy
class readexcel (object):
    @staticmethod
    def open_excel(self,file='file.xls'):
        try:
            data = xlrd.open_workbook(file)
            return data
        except Exception, e:
            print str(e)

    @classmethod
    def excel_table_byindex(self,file='file.xls', colnameindex=0, by_index=0):
        data = xlrd.open_workbook(file)
        # data = self.open_excel(file)
        table = data.sheets()[by_index]
        nrows = table.nrows
        colnames = table.row_values(colnameindex)
        list = []
        for rownum in range(1, nrows):
            row = table.row_values(rownum)
            if row:
                app = {}

                for i in range(len(colnames)):
                    app[colnames[i]] = row[i]
                list.append(app)
        return list
a =readexcel()
listdata1 = a.excel_table_byindex("1.xls", 0, 0)

workbook = xlwt.Workbook(encoding='ascii')

worksheet = workbook.add_sheet('My Worksheet',cell_overwrite_ok=True)
print( listdata1[877]['test'])
if ( str(listdata1[877]['test'])) is "否":
    print(111)
# for a in    range(0,len(listdata1)):
#     # print(a)
#     # print (listdata1[2299]['com'])
#
#     if  listdata1[a]['com'] == "":
#         print listdata1[a]['com']
#         if listdata1[a]['keep']:
#             listdata1[a]['com']=listdata1[a]['keep']
#             worksheet.write(a, 3, label=listdata1[a]['com'])
#         if listdata1[a]['test'] is '是' or listdata1[a]['test'] is '否':
#             print("111")
#             listdata1[a]['com'] = listdata1[a]['test']
#             worksheet.write(a, 3, label=listdata1[a]['com'])
#      # print(listdata1[a]['LIST1'])
#
#     worksheet.write(a, 3, label=listdata1[a]['com'])

# workbook.save('Excel_Workbook.xls')
# a=(listdata2[2]['keep'])
# print(a)
# b=(listdata1[4400]['com'])
# if  a== b :
#     print('yes')