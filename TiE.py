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
class TiE():
    @classmethod
    def Tie(self):
        token = weblogin.gettoken.token()
        taskId1 = getsql.sql.ChuShenID()[1]
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        # print(taskId1)

        for i in range(0,len(taskId1)):
            taskId=taskId1[i]

            headers = api.API.SetHeaders()
            payload1={
                 "data": {
                     "moduleCode": "audit",
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
            url3 = api.API.SetUrl()+"work/receiveTask"
            data = json.dumps(payload1)
            response = requests.request("POST", url3, data=data, headers=headers)
            response.text1 = json.loads(response.text)
            customer = getsql.sql.GetName()[i]
            print ("主贷人:" + customer + "  初审领取:" + response.text1["header"]["msg"][0])

            payload2 ={
	"data": {
		"ccSystemType": "",
		"otherContacts": None,
		"carAuto": "",
		"carCapacity": None,
		"carMileage": None,
		"carColor": None,
		"carAge": "一年以下",
		"carSkylight": None,
		"carConfig": None,
		"environment": "国1",
		"carDealer": "21313",
		"aaa": [8, 131],
		"vin": "123213123123",
		"regdate": "2018-06",
		"price": 0,
		"gearBox": "自动",
		"yearCheckDate": "2018-07",
		"buessCheckDate": "2018-08",
		"strongRiskDate": "2018-09",
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
		# "autohomeid": "LSVD000B111",
		"carRegisterDate": "2011-10-31",
		"terminalId": None,
		"loanRemark": None,
		"indoorAuditOpinion": None,
		"exAuditOpinion": None,
		"supplementOpinion": None,
		"sendBankRemark": None,
		"custName":  listdata1[i]['loanerName'],
		"custIdcard":  listdata1[i]['loanerCardId'],
		"custMobile": "18583266667",
		"salesmanName": "向进去/黄涛",
		"custMarriage": "1",
		"custNation": "汉族",
		"custRegister": "成都",
		"systemType": "1",
		"auditWay": "未知",
		"financeCost": "1222",
		"provinceCode": 110000,
		"areaGroup": "2",
		"carLicenseLocationProvinceCode": 120000,
		"riskAssessment": "1",
		"carModel": "AC Schnitzer/AC Schnitzer X6/2011款 ACS6 35i",
		"loanAmount": "22222",
		"driverLicenseFlag": "1",
		"replaceBuyFlag": "",
		"assessorAmount": 0.1999,
		"loanYear": "1",
		"loanRate": "22",
		"premium": "22",
		"otherCost": "22222",
		"gpsCost": "22222",
		"gpsQuantity": "2222",
		"payeeName": "测试收款人",
		"payeePhone": "18583255555",
		"payeeBankAmount": "12312312414",
		"payeeOpenBank": "23123123123",
		"insuranceCompany": "123123123",
		"carType": listdata1[i]['newcar'],
		"auditOpinion": "恶趣味群翁请问请问\n奥术大师大所大所多\n@！#！@#@！#\n23qeqwe",
		"taskId": taskId,
		"moduleCode": "audit",
		"cityCode": 110100,
		"countryCode": 110102,
		"carLicenseLocationCityCode": 120100
	},
	"header": {
		"app": " ",
		"gps": " ",
		"os": " ",
		"ver": " ",
		"token": token
	}
}
            url4 = api.API.SetUrl()+"work/handle/btnAhead"
            data = json.dumps(payload2)
            response = requests.request("POST", url4, data=data, headers=headers)
            response.text1 = json.loads(response.text)
            customer = getsql.sql.GetName()[i]
            print ("主贷人:" + customer + "  初审员提额:" + response.text1["header"]["msg"][0])
            # print(response.text)

# a=TiE.Tie()
