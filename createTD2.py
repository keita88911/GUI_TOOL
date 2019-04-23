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
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)

        token=applogin.gettoken.token()
        # token1=token.token()
        # # token1=str(token)


        for i in range(0, len(listdata1)):

            # print(token)
            headers = {'Content-Type': "application/json", }
            url = api.API.SetUrl()+"v1/app/business/create"
            newcar=int(listdata1[i]['newcar'])
            # print(newcar)
            # print(type(newcar))
            if newcar == 1:
                print(u"新车")
                payload = {
                            # "autohomeid": "AE0A0024111",
                            "carModel": "2004款 2.0T Spark",
                    "coupleName": "测试配偶",
                    "loanerCardPath1": "erp/230127198301158608/IDF89c233a8aaa846b13e747692b153dd4d.jpg",
                    "loanerCreditPath": "erp/230127198301158608/LEe2c50b7894cbe61abcbaa463036098f5.jpg",
                    "loanerCardPath2": "erp/230127198301158608/IDBd7e0beb614f0979a7a8ad1bd5326d3a7.jpg",
                    "phone": "18583287566",
                    "guarantorCardPath1": "erp/350602198107218379/IDGF26dea429d94a5dda5964622e9625d18e.jpg",
                    "loanerCardId": "142627197705140490",
                    "coupleCardPath1": "erp/500103199811301442/IDSFd5baba6f6d08cc2aeb5d491473b952b4.jpg",
                    "coupleCreditPath": "erp/500103199811301442/LES81fc85951855016d06ea65ba8707b11d.jpg",
                    "loanerPhone": "18583211111",
                    "loanerSignPath": "erp/230127198301158608/APa6295f90e1484c10966f64edfae48ad2.jpg",
                    "coupleCardPath2": "erp/500103199811301442/IDSB266e030e8d18314ca9519210c59fc0c4.jpg",
                    "loanChannel": 1,
                    "coupleSignPath": "erp/500103199811301442/APSd987fe54fd240c56ade4ec70c789a4d2.jpg",
                    "guarantorFlag": 1,
                    "guarantorSignPath": "erp/350602198107218379/APG9e65de128199de18c93c2c7048fb390b.jpg",
                    "guarantorCreditPath": "erp/350602198107218379/LEG7cc93db008d1925f30d3cc77e14d1cf7.jpg",
                    "guarantorName": "测试担保人",
                    "os": "android",
                    "loanerName": "测试主贷人",
                    "guarantorCardId": "511501198711131084",
                    "guarantorPhone": "18583287333",

                    "coupleFlag": 1,
                    "coupleCardId": "420113197805246719",
                    "guarantorCardPath2": "erp/350602198107218379/IDGB65c912323e5b4a18d8419043492a18cd.jpg",
                    "loanAmountType": "1",
                    "couplePhone": "18583222222",
                           "newcar":listdata1[i]['newcar'],
                           "token": token}
            else:
                print("二手车")
                payload = {

                    "loanerCardPath1": "erp/230127198301158608/IDF89c233a8aaa846b13e747692b153dd4d.jpg",
                    "loanerCreditPath": "erp/230127198301158608/LEe2c50b7894cbe61abcbaa463036098f5.jpg",
                    "loanerCardPath2": "erp/230127198301158608/IDBd7e0beb614f0979a7a8ad1bd5326d3a7.jpg",

                    "guarantorCardPath1": "erp/350602198107218379/IDGF26dea429d94a5dda5964622e9625d18e.jpg",

                    "coupleCardPath1": "erp/500103199811301442/IDSFd5baba6f6d08cc2aeb5d491473b952b4.jpg",
                    "coupleCreditPath": "erp/500103199811301442/LES81fc85951855016d06ea65ba8707b11d.jpg",

                    "loanerSignPath": "erp/230127198301158608/APa6295f90e1484c10966f64edfae48ad2.jpg",
                    "coupleCardPath2": "erp/500103199811301442/IDSB266e030e8d18314ca9519210c59fc0c4.jpg",
                    "loanChannel": 1,
                    "coupleSignPath": "erp/500103199811301442/APSd987fe54fd240c56ade4ec70c789a4d2.jpg",
                    "guarantorFlag": 1,
                    "guarantorSignPath": "erp/350602198107218379/APG9e65de128199de18c93c2c7048fb390b.jpg",
                    "guarantorCreditPath": "erp/350602198107218379/LEG7cc93db008d1925f30d3cc77e14d1cf7.jpg",

                    "os": "android",
                    "loanerName": "主贷人",
                    "loanerCardId": "130201197510172274",
                    "loanerPhone": "13404771025",

                    "guarantorName": "担保人",
                    "guarantorCardId": "622800199703019245",
                    "guarantorPhone": "18583222222",

                    "coupleName": "配偶",
                    "coupleCardId": "350421200003293225",
                    "phone": "15982703164",

                    "coupleFlag": 1,

                    "guarantorCardPath2": "erp/350602198107218379/IDGB65c912323e5b4a18d8419043492a18cd.jpg",
                    "loanAmountType": "1",
                    "couplePhone": "18583222222",
                           "newcar":listdata1[i]['newcar'],
                           "token": token}
            data = json.dumps(payload)
            response = requests.request("POST", url, data=data, headers=headers)
            # r = requests.post(url,data=payload,headers= headers)
            # response.text1 = json.loads(response.text)
            # customer=listdata1[i]['loanerName']
            #
            # print ("主贷人:"+customer+"  发起订单:"+response.text1["msg"])
            print response.text
            # if response.text1["msg"]!= "操作成功":
            #     sys.exit()
# a=create()
# a.addTD()