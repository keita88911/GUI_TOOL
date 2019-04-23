#coding=utf-8

import xlrd
import rdexcel



class GettoNode():
    @classmethod
    def GetNewcar(self):
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        listcar = []
        for i in range(0, len(listdata1)):
            listcar.append(listdata1[i]['newcar'])
            # print(listcar[i])
        return listcar

    @classmethod
    def a(self):
        newcar=GettoNode.GetNewcar()
        for i in range(0, len(newcar)):
            print(int(newcar[i]))
            if int(newcar[i])==0:
                print("旧车")
        print("ceshi")



b=GettoNode.a()
# listdata1 = a.excel_table_byindex("add1.xlsx", 0)
# listcar=[]
# for i in range(0, len(listdata1)):
#
#     listcar.append(listdata1[i]['newcar'])
#     print(listcar[i])
# print(type(listcar[0]))
