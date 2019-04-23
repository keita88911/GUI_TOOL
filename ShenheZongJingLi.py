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
class ShenheZongJingLi():

    @classmethod
    def ShenHeZongJL(self):
        token = weblogin.gettoken.token()
        taskId1 = getsql.sql.getsqldata()[1]
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        # print(taskId1)
        for i in range(0,len(listdata1)):
            if int(listdata1[i]['loanAmount']) >= 150000 :
                taskId=taskId1[i]
                headers = api.API.SetHeaders()
                payload1={
                     "data": {
                         "moduleCode": "generalManagerAudit",
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
                print ("主贷人:" + customer + "  总经理审核领取:" + response.text1["header"]["msg"][0])

                payload2 ={
        "data": {
            "lowLoan": "0",
            "isSeparate": "1",
            "firstPayment": 95200,
            "custName":listdata1[i]['loanerName'],
            "custIdcard": listdata1[i]['loanerCardId'],
            "custMobile": listdata1[i]['mobile'],
            "salesmanName": "向进/黄涛",
            "custMarriage": "1",
            "custNation": "汉族",
            "custRegister": "成都",
            "systemType": "1",
            "ccSystemType": "",
            "auditWay": "电审",
            "financeCost": 111,
            "provinceCode": 110000,
            "areaGroup": "1",
            "regdate":"2018-06",
            "strongRiskDate":"2018-09",
            "payeeName": "重庆市野峰汽车销售有限公司",
            "payeePhone": "18583287565",
            "custCompany": "成都工作单位",
            "carLicenseLocationProvinceCode": 110000,
            "riskAssessment": "1",
            "carModel": "AC Schnitzer/AC Schnitzer X6/2011款 ACS6 35i",
            "loanAmount": listdata1[i]['loanAmount'],
            "driverLicenseFlag": "1",
            "replaceBuyFlag": "",
            "assessorAmount": "18000",
            "loanYear": "3",
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
            "carType": listdata1[i]['newcar'],
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
            "indoorAuditOpinion": None,
            "exAuditOpinion": None,
            "auditOpinion": "请问请问无群二群翁请问请问请问请问123123123123 奥术大师大所阿萨德按时 新增操作从自行车征信",
            "supplementOpinion": "请问请问群无切请问额\n12312321312\n12312321切尔奇翁\n123123213",
            "sendBankRemark": None,
            "taskId": taskId,
            "completed": "true",
            "push": "false",
            "city":"131",
            "cityCode": 110100,
            "countryCode": 110101,
            "carLicenseLocationCityCode": 110100,
            "carLicenseLocationCountryCode": 110101,
            "yearCheckDate":"2018 - 07"
        },
        "header": {
            "app": " ",
            "gps": " ",
            "os": " ",
            "ver": " ",
            "token": token
        }
    }
                url4 = api.API.SetUrl() + "work/handle/generalManagerAudit"
                data = json.dumps(payload2)
                response = requests.request("POST", url4, data=data, headers=headers)
                response.text1 = json.loads(response.text)
                customer = getsql.sql.GetName()[i]
                print ("主贷人:" + customer + "  总经理审核:" + response.text1["header"]["msg"][0])
