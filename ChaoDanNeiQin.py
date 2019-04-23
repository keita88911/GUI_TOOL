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
class ChaoDanNeiQin():
    @classmethod
    def ChaoDanNeiQ(self):
        token = weblogin.gettoken.token()
        taskId1 = getsql.sql.getsqldata()[1]
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        # print(taskId1)
        for i in range(0, len(taskId1)):
            taskId = taskId1[i]
            headers = api.API.SetHeaders()
            payload1 = {
                "data": {
                    "moduleCode": "transcribeOrderOfInsider",
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
            print ("主贷人:" + customer + "  抄单内勤领取:" + response.text1["header"]["msg"][0])

            payload2={
    "data": {
        "custName":  listdata1[i]['loanerName'],
        "custIdcard": listdata1[i]['loanerCardId'],
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
        "carModel": "大巴",
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
        "auditOpinion": "请问请问无群二群翁请问请问请问请问123123123123 奥术大师大所阿萨德按时 新增操作从自行车征信",
        "supplementOpinion": "请问请问群无切请问额\n12312321312\n12312321切尔奇翁\n123123213",
        "sendBankRemark": "送行备注！@#@！#！@#12321312312阿尔大大送行备注！@#@！#！@#12321312312阿尔大大送行备注！@#@！#！@#12321312312阿尔大大送行备注！@#@！#！@#12321312312阿尔大大\n奥术大师大所 啊撒大声地\n3213123",
        "handleRemark": "测试备注奥术大师大所阿萨德按时d\n123！@#@！#！@#！@",
        "taskId": taskId,
        "completed": "true",
        "push": "false",
        "ccInfoPaperMaterial": None,
        "ccInfoQualificationMaterial": None,
        "ccDealPaperMaterial": [{
            "code": "SV",
            "name": "签单视频",
            "meterialType": 3,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": None,
            "serialNum": 340,
            "linkType": 1,
            "updateFlag": None,
            "optionalFlag": 0,
            "urlListCode": None
        }, {
            "code": "QAV",
            "name": "问答视频",
            "meterialType": 3,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": None,
            "serialNum": 350,
            "linkType": 1,
            "updateFlag": None,
            "optionalFlag": 0,
            "urlListCode": None
        }, {
            "code": "HV",
            "name": "家访视频",
            "meterialType": 3,
            "enableFlag": 0,
            "remark": None,
            "existFlag": 0,
            "urlList": None,
            "serialNum": 670,
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
            url4 = api.API.SetUrl() + "work/handle/ccDeal"
            data = json.dumps(payload2)
            response = requests.request("POST", url4, data=data, headers=headers)
            response.text1 = json.loads(response.text)
            customer = getsql.sql.GetName()[i]
            # print(taskId)
            print ("主贷人:" + customer + "  抄单内勤审核:" + response.text1["header"]["msg"][0])
# a=ChaoDanNeiQin.ChaoDanNeiQ()