# -*- coding: UTF-8 -*-
import rdexcel
import requests
import json
import weblogin
import MySQLdb
import getsql
import api
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class Province():
    @classmethod
    def province(self):

        if getsql.sql.Province():
            token = weblogin.gettoken.provincetoken()
            taskId1 = getsql.sql.auto("省区经理审核")[1]
            a = rdexcel.readexcel()
            listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
            # print(taskId1)
            for i in range(0, len(taskId1)):
                taskId = taskId1[i]
                headers = api.API.SetHeaders()
                payload1 = {
                "data": {
                    "moduleCode": "proAreaManagerAudit",
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
                print ("主贷人:" + customer + "  省区审核领取:" + response.text1["header"]["msg"][0])

                payload2 = {
                    "data": {
                        "lowLoan": "0",
                        "isSeparate": "1",
                        "firstPayment": 95200,
                        "custName": listdata1[i]['loanerName'],
                        "custIdcard": listdata1[i]['loanerCardId'],
                        "custMobile": listdata1[i]['mobile'],
                        "salesmanName": "向进/测试",
                        "custMarriage": "1",
                        "custNation": "汉族",
                        "custRegister": "成都",
                        "custRegisterAddress": None,
                        "systemType": "1",
                        "ccSystemType": "",
                        "auditWay": "电审",
                        "financeCost": 111,
                        "provinceCode": 110000,
                        "areaGroup": "1",
                        "carLicenseLocationProvinceCode": 110000,
                        "regdate": "2018-05",
                        "riskAssessment": "1",
                        "carModel": "AC Schnitzer/AC Schnitzer X6/2011款 ACS6 35i",
                        "loanAmount": 80000,
                        "driverLicenseFlag": "1",
                        "replaceBuyFlag": "",
                        "assessorAmount": 1999,
                        "loanYear": "2",
                        "custCompany": "成都工作单位",
                        "loanRate": 11,
                        "premium": 1111,
                        "otherCost": 111111,
                        "gpsCost": 1111,
                        "gpsQuantity": 11223,
                        "payeeName": "重庆市野峰汽车销售有限公司",
                        "payeePhone": "18583287565",
                        "payeeBankAmount": "2222222",
                        "payeeOpenBank": "111112",
                        "insuranceCompany": "1111233",
                        "otherContacts": None,
                        "carType": "0",
                        "carAuto": "",
                        "carColor": None,
                        "carAge": "一年以下",
                        "carSkylight": None,
                        "carConfig": None,
                        "environment": "国1",
                        "carDealer": "21313",
                        "aaa": [8, 131],
                        "vin": "123213123123",
                        "gearBox": "自动",
                        "yearCheckDate": "2018-07",
                        "buessCheckDate": "2018-08",
                        "strongRiskDate": "2018-09",
                        "sgNo": None,
                        "reportNo": None,
                        "appraisalTime": None,
                        "carVin": None,
                        "evaluationCompany": "东方航空公司",
                        "payerName": None,
                        "loanTime": None,
                        "address": None,
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
                        "exRelation": None,
                        "carRegisterDate": "2011-10-31",
                        "terminalId": None,
                        "loanRemark": None,
                        "indoorAuditOpinion": None,
                        "exAuditOpinion": None,
                        "auditOpinion": "请问请问无群二群翁请问请问请问请问123123123123 奥术大师大所阿萨德按时 新增操作从自行车征信",
                        "supplementOpinion": None,
                        "sendBankRemark": None,
                        "price": 0,
                        "province": 8,
                        "city": 131,
                        "toPaymentPool": 0,
                        "cback": True,
                        "taskId": taskId,
                        "completed": True,
                        "push": False,
                        "cityCode": 110100,
                        "countryCode": 110101,
                        "carLicenseLocationCityCode": 110100
                    },
                    "header": {
                        "app": " ",
                        "gps": " ",
                        "os": " ",
                        "ver": " ",
                        "token": token
                    }
                }
                url4 = api.API.SetUrl() + "work/handle/proAreaManagerAudit"
                data = json.dumps(payload2)
                response = requests.request("POST", url4, data=data, headers=headers)
                response.text1 = json.loads(response.text)
                customer = getsql.sql.GetName()[i]
                print ("主贷人:" + customer + "  省区审核:" + response.text1["header"]["msg"][0])
# a=Province.province()