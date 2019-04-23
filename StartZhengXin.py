# -*- coding: UTF-8 -*-
import rdexcel
import requests
import json
import weblogin
import  MySQLdb
import getsql
import api
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
class StartZhengXin():
    @classmethod
    def StartZhengXin(self):
        token = weblogin.gettoken.token()
        taskId1 = getsql.sql.StartZhengXin()

        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        # print(taskId1)
        if taskId1:
            print("此订单征信不通过，工具即将自动重启至驻行部")
            for i in range(0, len(taskId1)):
                # print("1")
                # p = taskId1[i]
                headers = api.API.SetHeaders()


                payload2={
	"data": taskId1[0],
	"header": {
		"app": " ",
		"gps": " ",
		"os": " ",
		"ver": " ",
		"token": token
	}
}
                url4 = api.API.SetUrl() + "creditManager/updateCreditAdopt"
                data = json.dumps(payload2)
                response = requests.request("POST", url4, data=data, headers=headers)
                response.text1 = json.loads(response.text)
                customer = getsql.sql.GetName()[i]
                # print(response.text)
                print ("主贷人:" + customer + "  重启结果:" + response.text1["header"]["msg"][0])
# a=StartZhengXin.StartZhengXin()