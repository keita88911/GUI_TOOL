import requests
import json
import api
import rdexcel

class gettoken():
    @classmethod
    def token (self):
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_bysheet("add1.xlsx", 0, 0)
        for i in range(0, len(listdata1)):
            headers = api.API.SetHeaders()
            url1 = api.API.SetUrl()+"login"
            data1 = {"data": {"password":listdata1[i]['WebPassword'],"username": listdata1[i]['WebUsername']}}
            para1 = json.dumps(data1)

            r=requests.post(url1,data=para1,headers= headers)
            token = r.cookies.items()[0][1]
            # print(token)
            return (token)
    @classmethod
    def JingLintoken(self):
        headers = api.API.SetHeaders()
        url1 = api.API.SetUrl()+"login"
        data1 = {"data": {"password": "12345678","username": "18583287566"}}
        para1 = json.dumps(data1)
        r=requests.post(url1,data=para1,headers= headers)

        token = r.cookies.items()[0][1]
        # print(token)
        return (token)
    @classmethod
    def ZhuHangSStoken(self):
        headers = api.API.SetHeaders()
        url1 = api.API.SetUrl()+"login"
        data1 = {"data": {"password": "12345678","username": "18583287560"}}
        para1 = json.dumps(data1)
        r=requests.post(url1,data=para1,headers= headers)
        token = r.cookies.items()[0][1]
        # print(token)
        return (token)
    @classmethod
    def provincetoken (self):
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_bysheet("add1.xlsx", 0, 0)
        for i in range(0, len(listdata1)):
            headers = api.API.SetHeaders()
            url1 = api.API.SetUrl()+"login"
            data1 = {"data": {"password":listdata1[i]['ProvinPassword'],"username": listdata1[i]['Provin']}}
            para1 = json.dumps(data1)
            r=requests.post(url1,data=para1,headers= headers)
            # r1=json.loads(r.text)
            # print(r.text)
            token = r.cookies.items()[0][1]
            # print(r1['data']['token'])
            # print(token)
            return (token)

        @classmethod
        def provincetoken(self):
            a = rdexcel.readexcel()
            listdata1 = a.excel_table_bysheet("add1.xlsx", 0, 0)
            for i in range(0, len(listdata1)):
                headers = api.API.SetHeaders()
                url1 = api.API.SetUrl() + "login"
                data1 = {"data": {"password": listdata1[i]['ProvinPassword'], "username": listdata1[i]['Provin']}}
                para1 = json.dumps(data1)
                r = requests.post(url1, data=para1, headers=headers)
                # r1=json.loads(r.text)
                # print(r.text)
                token = r.cookies.items()[0][1]
                # print(r1['data']['token'])
                # print(token)
                return (token)
# a=gettoken.provincetoken()
# a=gettoken.JingLintoken()
