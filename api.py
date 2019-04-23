# -*- coding: UTF-8 -*-
import rdexcel


class API():

    @classmethod
    def SetUrl(self):
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_bysheet("add1.xlsx", 0, 0)
        url=[]
        for i in range(0, len(listdata1)):
            url=listdata1[i]['API']
            # print( url)
            return  url

    @classmethod
    def SetHeaders(self):
        headers={
                'Content-Type': "application/json",
            }
        return headers
# a=API.SetUrl()