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
class ChuNaDianKuan():
    @classmethod
    def ChuNaDianKuan(self):
        token = weblogin.gettoken.token()
        taskId1 = getsql.sql.ChuNaDianKuan()[1]
        a = rdexcel.readexcel()
        listdata1 = a.excel_table_byindex("add1.xlsx", 0, 0)
        # print(taskId1)
        for i in range(0, len(taskId1)):
            taskId = taskId1[i]
            headers = api.API.SetHeaders()
            payload1 = {
                "data": {
                    "moduleCode": "cashierAdvance",
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
            print ("主贷人:" + customer + "  出纳垫款领取:" + response.text1["header"]["msg"][0])

            payload2={
	"data": {
        "custName": listdata1[i]['loanerName'],
        "custIdcard": listdata1[i]['loanerCardId'],
		"custMobile": "18583266667",
		"salesmanName": "向进/高家源",
		"custMarriage": "1",
		"custNation": "汉族",
		"custRegister": "成都",
		"custRegisterAddress": None,
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
		"assessorAmount": 18000,
		"loanYear": "3",
		"loanRate": 11,
		"premium": 1111,
		"otherCost": 111111,
		"gpsCost": 1111,
		"gpsQuantity": 11223,
		"payeeName": "测试收款人",
		"payeePhone": "11112233333",
		"payeeBankAmount": "6225881287543051",
		"payeeOpenBank": "测试开户行",
		"insuranceCompany": "1111233",
		"otherContacts": None,
		"carType": "0",
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
		"autohomeid": None,
		"carRegisterDate": "2011-10-31",
		"terminalId": None,
		"loanRemark": None,
		"indoorAuditOpinion": "测试审核备注12312321#!@#@!!@#@!#\nASDASDASD",
		"exAuditOpinion": None,
		"auditOpinion": "请问请问无群二群翁请问请问请问请问123123123123 奥术大师大所阿萨德按时 新增操作从自行车征信",
		"supplementOpinion": "请问请问群无切请问额\n12312321312\n12312321切尔奇翁\n123123213",
		"sendBankRemark": None,
		"rebate": "2",
		"actualPay": "20000",
		"payerName": "测试付款人",
		"loanTime": "2018-08-02",
		"actualFinanceCost": "20000",
		"handleRemark": "艾维奇翁群无",
		"province": 8,
		"city": 131,
		"taskId": taskId,
		"completed": "true",
		"push": "false",
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
            url4 = api.API.SetUrl() + "work/handle/cashierAdvance"
            data = json.dumps(payload2)
            response = requests.request("POST", url4, data=data, headers=headers)
            response.text1 = json.loads(response.text)
            customer = getsql.sql.GetName()[i]
            # print(response.text)
            print ("主贷人:" + customer + "  出纳垫款审核:" + response.text1["header"]["msg"][0])
# a=ChuNaDianKuan.ChuNaDianKuan()