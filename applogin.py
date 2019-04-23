# -*- coding: UTF-8 -*-
import requests
import json
import api
import rdexcel
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

class gettoken():

    @classmethod
    def token(self):
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_bysheet("add1.xlsx", 0, 0)
        for i in range(0, len(listdata1)):
            headers = {'Content-Type': "application/json", }
            url1 = api.API.SetUrl()+"v1/app/login"
            # print(url1)
            data1 = {"data": {"password": listdata1[i]['Password'], "username": listdata1[i]['AppUsername']}}
            para1 = json.dumps(data1)
            r = requests.post(url1, data=para1, headers=headers)
            jas1 = r.text
            result = jas1.encode('utf-8')
            jd = json.loads(result)

            if jd['header']['msg'][0] in "登录成功":
                # print("APP登录成功")
                tokenID = jd["data"]["token"]
                return (tokenID)
            else:
                print("APP登录失败")
                exit()
                return False
#
# a=gettoken()
# a.token()
# print a.token()
# print(type(a.token()))