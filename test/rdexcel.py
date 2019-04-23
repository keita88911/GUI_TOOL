#coding=utf-8

import xlrd
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
# a=readexcel ()
# listdata1 = a.excel_table_byindex("D:\\add1.xlsx", 0)
# for i in range(0, len(listdata1)):
#     listdata1[i]['loanerName']
#     print(listdata1[i]['loanerName'])