#!usr/bin/python
# -*- coding: utf-8 -*-
import applogin
import rdexcel
import requests
import json
import applogin
import sys
import api
import getsql

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class create():
    @classmethod
    def addTD(self):
        print(u'友情提示：若为快贷订单，月收入，车架号，征信等相关信息将被系统默认修改')
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)

        token = applogin.gettoken.token()
        # token1=token.token()
        # # token1=str(token)

        for i in range(0, len(listdata1)):
            # print("totoal"+str(i))
            # print( listdata1[i]['fast_loan'])
            if listdata1[i]['fast_loan'] == "1":
                # print("快贷订单")
                headers = {'Content-Type': "application/json", }  # 读取接口相关信息
                url = api.API.SetUrl() + "v1/app/business/create"
                newcar = int(listdata1[i]['newcar'])
                # print(newcar)
                # print(type(newcar))
                if newcar == 1:  # 判断新旧车
                    # print(u"新车")

                    print(u"新车不能进入快贷")
                    exit()
                    return False
                else:
                    # print("快贷二手车")
                    payload = {
                        "workPlace": "四川成都高新",  # 公司
                        "residencePlace": "四川成都高新",  # 居住地
                        "custCompany": "联通",  # 工作单位
                        "coupleFlag": "0",
                        "guarantorFlag": "0",
                        "loanAmountType": "1",
                        "custIncome": listdata1[i]['custIncome'],  # 月收入
                        "autochthon": listdata1[i]['autochthon'],  # 0 非本地人 ，1本地人
                        "loanChannel": listdata1[i]['loanChannel'],
                        "loanerCardId": listdata1[i]['loanerCardId'],
                        "loanerCardPath1": "erp/61444/LPPA03e0900cdafe7bf0262d88273f5295b2.jpg",
                        "loanerCardPath2": "erp/510104198806031672/IDBe423f7dfa12298159d05816a34efe81f.jpg",
                        "loanerCreditPath": "erp/510104198806031672/LE58583af34c31202acc9bf3a3709bad08.jpg",
                        "loanerName": listdata1[i]['loanerName'],
                        "loanerPhone": listdata1[i]['mobile'],
                        "loanerSignPath": "erp/510104198806031672/AP5b9708d50f9f8d8b1b2ef0cb82785e20.jpg",
                        "os": "android",
                        "phone": "18583287560",
                        "newcar": listdata1[i]['newcar'],
                        "token": token}
                data = json.dumps(payload)
                response = requests.request("POST", url, data=data, headers=headers)
                # r = requests.post(url,data=payload,headers= headers)
                response.text1 = json.loads(response.text)
                customer = listdata1[i]['loanerName']
                #
                print ("主贷人:" + customer + "  发起订单:" + response.text1["msg"])
            else:


                # print(token)
                headers = {'Content-Type': "application/json", }  # 读取接口相关信息
                url = api.API.SetUrl() + "v1/app/business/create"
                newcar = int(listdata1[i]['newcar'])
                # print(newcar)
                # print(type(newcar))
                if newcar == 1:  # 判断新旧车
                    # print(u"新车")
                    payload = {
                        "workPlace":"四川成都高新",#公司
                    "residencePlace":"四川成都高新",#居住地
                    "custCompany":"联通",#工作单位

                        # "autohomeid": "LSVD000B111",
                        "custIncome": listdata1[i]['custIncome'],  # 月收入
                        "autochthon": listdata1[i]['autochthon'],  # 0 非本地人 ，1本地人
                        "carModel": "奔驰/102",
                        "coupleFlag": "0",
                        "guarantorFlag": "0",

                        "loanAmountType": "1",
                        "loanChannel": listdata1[i]['loanChannel'],   #1 工行 2 农行
                        "loanerCardId": listdata1[i]['loanerCardId'],
                        # "loanerCardPath1": "erp/510104198806031672/IDF18ca204cbcc227b20d836d55059ab6b8.jpg",
                        "loanerCardPath1": "erp/61444/LPPA03e0900cdafe7bf0262d88273f5295b2.jpg",
                        "loanerCardPath2": "erp/510104198806031672/IDBe423f7dfa12298159d05816a34efe81f.jpg",
                        "loanerCreditPath": "erp/510104198806031672/LE58583af34c31202acc9bf3a3709bad08.jpg",
                        "loanerName": listdata1[i]['loanerName'],
                        "loanerPhone": listdata1[i]['mobile'],
                        "loanerSignPath": "erp/510104198806031672/AP5b9708d50f9f8d8b1b2ef0cb82785e20.jpg",
                        "os": "android",
                        "phone": "18583287560",
                        "newcar": listdata1[i]['newcar'],
                        "token": token}
                else:
                    # print("二手车")
                    payload = {
                        "workPlace": "四川成都高新",  # 公司
                        "residencePlace": "四川成都高新",  # 居住地
                        "custCompany": "联通",  # 工作单位

                        "coupleFlag": "0",
                        "guarantorFlag": "0",
                        "loanAmountType": "1",
                        "custIncome":listdata1[i]['custIncome'],  # 月收入
                        "autochthon": listdata1[i]['autochthon'],  # 0 非本地人 ，1本地人
                        "loanChannel": listdata1[i]['loanChannel'],
                        "loanerCardId": listdata1[i]['loanerCardId'],
                        "loanerCardPath1": "erp/61444/LPPA03e0900cdafe7bf0262d88273f5295b2.jpg",
                        "loanerCardPath2": "erp/510104198806031672/IDBe423f7dfa12298159d05816a34efe81f.jpg",
                        "loanerCreditPath": "erp/510104198806031672/LE58583af34c31202acc9bf3a3709bad08.jpg",
                        "loanerName": listdata1[i]['loanerName'],
                        "loanerPhone": listdata1[i]['mobile'],
                        "loanerSignPath": "erp/510104198806031672/AP5b9708d50f9f8d8b1b2ef0cb82785e20.jpg",
                        "os": "android",
                        "phone": "18583287560",
                        "newcar": listdata1[i]['newcar'],
                        "token": token}
                data = json.dumps(payload)
                print(str(data).replace('u\'', '\'').decode('unicode_escape'))
                response = requests.request("POST", url, data=data, headers=headers)
                # r = requests.post(url,data=payload,headers= headers)
                response.text1 = json.loads(response.text)
                customer = listdata1[i]['loanerName']
                # print( response.text)
                print ("主贷人:" + customer + "  发起订单:" + response.text1["msg"])
            # print response.text
            # if response.text1["msg"]!= "操作成功":
            #     sys.exit()
# a=create()
# a.addTD()
