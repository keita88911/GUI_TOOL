#!usr/bin/python
# -*- coding: utf-8 -*-
import applogin
import rdexcel
import requests
import json
import applogin
import sys
import getsql
import api
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
class BuChongXinxi():
    @classmethod
    def BuChongxinxi(self):
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        token=applogin.gettoken.token()
        taskid1=getsql.sql.GetShenheHouBuChongID()[1]
        id1=getsql.sql.GetShenheHouBuChongID()[0]
        for i in range(0, len(taskid1)):
            id=id1[i]
            taskid=taskid1[i]
            # print(token)
            headers = {'Content-Type': "application/json", }
            url=api.API.SetUrl()+"v1/app/mytask/commitInfoAfterAudit"
            newcar=int(listdata1[i]['newcar'])
            # print(newcar)
            # print(type(newcar))
            if newcar == 1:
                payload={
                    "imageList": [{
                        "code": "ICFAC",
                        "path": "erp/11584/ICFAC6177c3a8c9dd6be88f0b2caaebfc3241.jpg"
                    }, {
                        "code": "NCC",
                        "path": "erp/11584/NCC687296b06700f86dcae3b49c3abc4d65.jpg"
                    }, {
                        "code": "ICFACC",
                        "path": "erp/11584/ICFACCa6b3a5ed7fd165671a2cad3a57981597.jpg"
                    }, {
                        "code": "RCMV",
                        "path": "erp/11584/RCMV389fe0a915fcdcdf4fad6c71f46167c4.jpg"
                    }, {
                        "code": "NCI",
                        "path": "erp/11584/NCIc8a56e78b18c4213e6d58f83d8991e9c.jpg"
                    }],
    "os": "android",
    "phone": "18583287560",
    "reqId": id,
    "step": 7,
    "taskId": taskid,
    "token": token
            }
            else:

                payload ={
        "phone": "18583287560",
        "reqId": id,
        "step": 7,
        "imageList": [{
            "code": "GPS",
            "path": "erp/12847/GPSd9d9b38e8ee6232050ee2abdaa4fc57a.jpg"
        }, {
            "code": "ICFAC",
            "path": "erp/12847/ICFAC1d36b19b3681ea0a25bbbf46521b766d.jpg"
        }, {
            "code": "ICFACC",
            "path": "erp/12847/ICFACCbbe17cc7a41c5f8e0d9bdb8403acb499.jpg"
        },
            {
            "code": "MVDLA",
            "path": "erp/12847/MVDLA3874c84bd0f0c43755c33ec908325002.jpg"
        },
            {
            "code": "LPPA",
            "path": "erp/12847/LPPAc46a385868f2350d9b85b90ff95a0655.jpg"
        }, {
            "code": "RCMVA",
            "path": "erp/12847/RCMVAb22ca574f26ef08e6f0c329192e9553f.jpg"
        }, {
            "code": "TLP",
            "path": "erp/12847/TLP571cb6f51424e313ccdfa5865afa899b.jpg"
        }, {
            "code": "PPA",
            "path": ""
        }, {
            "code": "TLP",
            "path": ""
        }, {
            "code": "INV",
            "path": ""
        }, {
            "code": "VOU",
            "path": ""
        }, {
            "code": "FV",
            "path": ""
        }, {
            "code": "FV",
            "path": ""
        }, {
            "code": "AA",
            "path": ""
        },
            {
                "code": "PMC",
                "path": "erp/10017/PMCd6c0ba52533a23f2d39db9c272057620.jpg"
            }
        ],
        "token": token,
        "os": "android",
        "taskId": taskid
    }
            data = json.dumps(payload)
            response = requests.request("POST", url, data=data, headers=headers)
            # r = requests.post(url,data=payload,headers= headers)
            response.text1 = json.loads(response.text)
            customer=getsql.sql.GetName()[i]

            print ("主贷人:"+customer+"  审核后补充资料:"+response.text1["msg"])
# a=BuChongXinxi.BuChongxinxi()