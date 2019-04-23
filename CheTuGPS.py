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
class CheTuGPS():
    @classmethod
    def GPS(self):
        token = weblogin.gettoken.token()
        taskId1 = getsql.sql.auto('车图GPS')[1]
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        # print(taskId1)
        for i in range(0, len(taskId1)):
            taskId = taskId1[i]

            headers = api.API.SetHeaders()
            payload1 = {
                "data": {
                    "moduleCode": "confirmInfo",
                    "taskId": taskId
                },
                "ext": "string",
                "header": {
                    "app": "string",
                    "gps": "string",
                    "os": "string",
                    "token": token,
                    "ver": "string"
                }
            }
            url3 = api.API.SetUrl() + "work/receiveTask"
            data = json.dumps(payload1)
            response = requests.request("POST", url3, data=data, headers=headers)
            response.text1 = json.loads(response.text)
            customer = getsql.sql.GetName()[i]
            print ("主贷人:" + customer + "  车图GPS领取:" + response.text1["header"]["msg"][0])

            payload2={
    "data": {
        "custName": listdata1[i]['loanerName'],
        "custIdcard":  listdata1[i]['loanerCardId'],
        "custMobile": "18583266667",
        "salesmanName": "向进/黄涛",
        "custMarriage": "1",
        "custNation": "汉族",
        "custRegister": "成都",
        "systemType": "1",
        "ccSystemType": "",
        "auditWay": "不知道",
        "financeCost": 111,
        "provinceCode": 110000,
        "areaGroup": "",
        "carLicenseLocationProvinceCode": 110000,
        "riskAssessment": "1",
        "carModel": "AC Schnitzer/AC Schnitzer X6/2011款 ACS6 35i",
        "loanAmount": 160000,
        "driverLicenseFlag": "",
        "replaceBuyFlag": "",
        "assessorAmount": "18000",
        "loanYear": "1",
        "loanRate": 11,
        "premium": 1111,
        "otherCost": 111111,
        "gpsCost": 1111,
        "gpsQuantity": 11223,
        "payeeName": "111123",
        "payeePhone": "11112233333",
        "payeeBankAmount": "2222222",
        "payeeOpenBank": "111112",
        "insuranceCompany": "1111233",
        "otherContacts": None,
        "carType": "0",
        "carAuto": "",
        "carCapacity": None,
        "carMileage": None,
        "carColor": None,
        "carSkylight": None,
        "carConfig": None,
        "carRegisterDate": None,
        "sgNo": None,
        "reportNo": None,
        "appraisalTime": None,
        "carVin": None,
        "rebate": None,
        "actualPay": None,
        "payerName": None,
        "loanTime": None,
        "address": None,
        "email": None,
        "mortgageArea": None,
        "other": None,
        "handleCardStatus": None,
        "subBankPassTime": None,
        "returnedMoneyDate": None,
        "cardBackTime": None,
        "bankBackTime": None,
        "cardNo": None,
        "transferName": "",
        "hasCarNum": "",
        "transcribeCarModel": None,
        "exCustName": None,
        "exCustIdcard": None,
        "exCustPhone": None,
        "exRelation": None,
        "loanRemark": None,
        "indoorAuditOpinion": "测试审核备注12312321#!@#@!!@#@!#\nASDASDASD",
        "exAuditOpinion": None,
        "auditOpinion": None,
        "supplementOpinion": None,
        "sendBankRemark": None,
        "handleRemark": "测试备注！@#@！#！@#@！#@！",
        "taskId": taskId,
        "completed": "true",
        "push": "false",
        "carMeterial": [{
            "code": "PPA",
            "name": "保单照片",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/4938/PPA78f3996089ae914f48599c02ce6ad8d0.jpg", "http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/4938/PPA70ea073a6b6e60aa1ee928a75331190b.jpg"],
            "serialNum": 360,
            "linkType": 1,
            "updateFlag": None,
            "optionalFlag": 0,
            "urlListCode": None
        }, {
            "code": "RCMVB",
            "name": "机动车登记证书(过户前)",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/RCMVB59ce9ca98d795f7cd8a6383dedde0aad.jpg"],
            "serialNum": 370,
            "linkType": 1,
            "updateFlag": 0,
            "optionalFlag": 0,
            "urlListCode": None
        }, {
            "code": "RCMVA",
            "name": "机动车登记证书(过户后)",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/4938/RCMVAa241e92052995ae0eaa7d720e7f3fb0c.jpg"],
            "serialNum": 380,
            "linkType": 1,
            "updateFlag": None,
            "optionalFlag": 0,
            "urlListCode": None
        }, {
            "code": "MVDLB",
            "name": "机动车行驶证(过户前)",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/MVDLBebe298e5889b77edc3e913c9c53ba304.jpg"],
            "serialNum": 390,
            "linkType": 1,
            "updateFlag": 0,
            "optionalFlag": 0,
            "urlListCode": None
        }, {
            "code": "MVDLA",
            "name": "机动车行驶证(过户后)",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/4938/MVDLA751e85b720bb1ed2e9ca45bb59c4afb0.jpg"],
            "serialNum": 400,
            "linkType": 1,
            "updateFlag": None,
            "optionalFlag": 0,
            "urlListCode": None
        }, {
            "code": "LPPA",
            "name": "车牌号照片(过户后)",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/4938/LPPA1cf695fa4ee56b77daf00fa0afa354c4.jpg"],
            "serialNum": 401,
            "linkType": 1,
            "updateFlag": None,
            "optionalFlag": 0,
            "urlListCode": None
        }, {
            "code": "LPPB",
            "name": "车牌号照片(过户前)",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/LPPB04c0053857b25515ef1329d1bb1fa993.jpg"],
            "serialNum": 402,
            "linkType": 1,
            "updateFlag": None,
            "optionalFlag": 0,
            "urlListCode": None
        }, {
            "code": "CFD",
            "name": "车辆正面照",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/CFDc7e652ef1ffa4692a8a085a789c4560a.jpg"],
            "serialNum": 470,
            "linkType": 1,
            "updateFlag": 0,
            "optionalFlag": 0,
            "urlListCode": None
        }, {
            "code": "COS",
            "name": "车辆斜侧面照",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/COSa0cef4fb8f94819cb5aeb6509969e06a.jpg"],
            "serialNum": 480,
            "linkType": 1,
            "updateFlag": None,
            "optionalFlag": 0,
            "urlListCode": None
        }, {
            "code": "CB",
            "name": "车尾正面",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/CBf14cc0a7ca956de9e68b3d77d4e83b51.jpg"],
            "serialNum": 490,
            "linkType": 1,
            "updateFlag": 0,
            "optionalFlag": 0,
            "urlListCode": None
        }, {
            "code": "PMC",
            "name": "人车合影",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/PMCaaf255cb29bf2a3ebe037d52b587a3ac.jpg"],
            "serialNum": 590,
            "linkType": 1,
            "updateFlag": None,
            "optionalFlag": 0,
            "urlListCode": None
        }, {
            "code": "ICFAC",
            "name": "身份证与车架号合影",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/ICFAC5d20735ff5274bed704f3e6ba101856c.jpg"],
            "serialNum": 600,
            "linkType": 1,
            "updateFlag": None,
            "optionalFlag": 0,
            "urlListCode": None
        }, {
            "code": "ICFACC",
            "name": "身份证与出厂牌合影",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/3908/ICFACCac6eda56575651957c6dadd74e76ee0c.jpg"],
            "serialNum": 601,
            "linkType": 1,
            "updateFlag": None,
            "optionalFlag": 0,
            "urlListCode": None
        }, {
            "code": "OPI",
            "name": "里程表照片",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/2219/OPI84362c9993bfdf505dc35165fd43b5ed.jpg"],
            "serialNum": 610,
            "linkType": 1,
            "updateFlag": 0,
            "optionalFlag": 0,
            "urlListCode": None
        }, {
            "code": "GPS",
            "name": "GPS照片",
            "meterialType": 2,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": ["http://hschefu-ivt.oss-cn-shenzhen.aliyuncs.com/res/erp/4938/GPSdf0ad68528ffc8091781a670a2a370ce.jpg"],
            "serialNum": 620,
            "linkType": 1,
            "updateFlag": None,
            "optionalFlag": 0,
            "urlListCode": None
        }],
        "cityCode": 110100,
        "countryCode": 110101,
        "carLicenseLocationCityCode": 110100,
        "carLicenseLocationCountryCode": 110101
    },
    "header": {
        "app": " ",
        "gps": " ",
        "os": " ",
        "ver": " ",
        "token": token
    }
}
            url4 = api.API.SetUrl() + "work/handle/confirmInfo"
            data = json.dumps(payload2)
            response = requests.request("POST", url4, data=data, headers=headers)
            response.text1 = json.loads(response.text)
            customer = getsql.sql.GetName()[i]
            print ("主贷人:" + customer + "  车图GPS审核:" + response.text1["header"]["msg"][0])
# a=CheTuGPS.GPS()